"""Build the thirty tabular datasets of CS 301, Unit II.

Every dataset comes from the UCI Machine Learning Repository and is licensed
CC BY 4.0. The script downloads each source file once into raw/ (not
committed), keeps the numeric columns named below, drops rows with a missing
value, and writes

    unit-2/data/NN-<name>.csv   one file per dataset, numeric columns only
    unit-2/data/datasets.csv    the list the notebooks read: number, file, title, size
    unit-2/data/SOURCES.md      where each file comes from, its licence, what was changed

A file that leaves this script has no missing value, no text column and no
constant column, so the standard deviation of every column is positive.

Run from the repository root:

    python tools/build_unit2_datasets.py            # build everything
    python tools/build_unit2_datasets.py 7 24       # only datasets 7 and 24
"""
import io
import json
import pathlib
import re
import sys
import urllib.request
import zipfile

import numpy as np
import pandas as pd

ROOT = pathlib.Path(__file__).resolve().parent.parent
RAW = ROOT / "raw"
OUT = ROOT / "unit-2" / "data"
UA = {"User-Agent": "Mozilla/5.0 (course material preparation)"}
UCI = "https://archive.ics.uci.edu"


# ---------------------------------------------------------------- downloads

def fetch(url, dest):
    """Download url to dest unless a non-empty copy is already there."""
    if dest.exists() and dest.stat().st_size > 0:
        return dest
    dest.parent.mkdir(parents=True, exist_ok=True)
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=300) as r, open(dest, "wb") as f:
        while True:
            chunk = r.read(1 << 20)
            if not chunk:
                break
            f.write(chunk)
    return dest


def metadata(uci_id):
    p = RAW / f"{uci_id}.json"
    fetch(f"{UCI}/api/dataset?id={uci_id}", p)
    return json.load(open(p, encoding="utf-8"))["data"]


def licence(uci_id, meta):
    """The licence sentence on the dataset's own page, e.g. '... (CC BY 4.0)'."""
    p = RAW / f"{uci_id}.html"
    fetch(meta["repository_url"], p)
    html = p.read_text(encoding="utf-8", errors="replace")
    m = re.search(r"This dataset is licensed under a(.{0,400}?)license\.", html, re.S)
    if not m:
        raise SystemExit(f"no licence statement found on the page of dataset {uci_id}")
    return re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", m.group(1))).strip()


def uci_csv(uci_id, **kw):
    """The single CSV that the repository serves for an imported dataset."""
    p = fetch(f"{UCI}/static/public/{uci_id}/data.csv", RAW / f"{uci_id}.csv")
    return pd.read_csv(p, low_memory=False, **kw)


def uci_zip(uci_id, meta):
    slug = meta["repository_url"].rstrip("/").split("/")[-1]
    return zipfile.ZipFile(fetch(f"{UCI}/static/public/{uci_id}/{slug}.zip", RAW / f"{uci_id}.zip"))


# ---------------------------------------------------------------- the thirty

def every(df, k):
    return df.iloc[::k]


def household(meta):
    df = uci_csv(235, na_values=["?"]).drop(columns=["Date", "Time"]).dropna()
    return every(df, 15)


def credit(meta):
    df = uci_csv(350).drop(columns=["ID", "Y"])
    names = {v["name"]: v["description"] for v in meta["variables"] if v.get("description")}
    return df.rename(columns=names)


def casp(meta):
    return pd.read_csv(uci_zip(265, meta).open("CASP.csv"))


def sgemm(meta):
    return every(pd.read_csv(uci_zip(440, meta).open("sgemm_product.csv")), 5)


def accelerometer(meta):
    return pd.read_csv(uci_zip(846, meta).open("accelerometer (1).csv"))


def beijing_station(meta):
    outer = uci_zip(501, meta)
    inner = zipfile.ZipFile(io.BytesIO(outer.read("PRSA2017_Data_20130301-20170228.zip")))
    name = "PRSA_Data_20130301-20170228/PRSA_Data_Aotizhongxin_20130301-20170228.csv"
    return pd.read_csv(inner.open(name)).drop(columns=["No", "wd", "station"]).dropna()


def crowdsourced(meta):
    return pd.read_csv(uci_zip(400, meta).open("training.csv")).drop(columns=["class"])


# number, file name, UCI id, title, what one row is, loader, what was changed
SPECS = [
    (1, "magic-gamma-telescope", 159, "MAGIC Gamma Telescope",
     "one simulated particle shower recorded by a gamma-ray telescope: ten measurements of its image",
     lambda m: uci_csv(159).drop(columns=["class"]),
     "The class column was removed."),
    (2, "pulsar-candidates", 372, "HTRU2 Pulsar Candidates",
     "one pulsar candidate from a radio survey of the sky: eight statistics of its signal",
     lambda m: uci_csv(372).drop(columns=["class"]),
     "The class column was removed."),
    (3, "appliances-energy", 374, "Appliances Energy Prediction",
     "one ten-minute reading in a house: energy used by appliances and lights, temperature and humidity in each room, and the weather outside",
     lambda m: uci_csv(374).drop(columns=["date"]),
     "The date column was removed."),
    (4, "superconductivity", 464, "Superconductivity Data",
     "one superconducting material: 81 features computed from its chemical formula, and its critical temperature",
     lambda m: every(uci_csv(464), 2),
     "Every second row was kept (10,632 of 21,263)."),
    (5, "gas-turbine-emissions", 551, "Gas Turbine CO and NOx Emission Data Set",
     "one hour of sensor measurements at a gas turbine, with its carbon monoxide and nitrogen oxide emissions",
     lambda m: uci_csv(551).drop(columns=["year"]),
     "The year column was removed."),
    (6, "bike-sharing-hourly", 275, "Bike Sharing",
     "one hour of a bike-sharing system in 2011 and 2012: calendar codes, weather, and the number of bikes rented",
     lambda m: uci_csv(275).drop(columns=["instant", "dteday"]),
     "The row counter and the date column were removed."),
    (7, "beijing-pm25", 381, "Beijing PM2.5",
     "one hour in Beijing, 2010 to 2014: the PM2.5 concentration of the air, the weather, and the date and hour as numbers",
     lambda m: uci_csv(381).drop(columns=["No", "cbwd"]).dropna(),
     "The row counter and the wind-direction column (text) were removed, and so were the 2,067 hours with no PM2.5 reading."),
    (8, "household-power", 235, "Individual Household Electric Power Consumption",
     "one minute of electricity measurements in one household, 2006 to 2010",
     household,
     "The date and time columns and the 25,979 minutes with missing measurements were removed; then every fifteenth row was kept."),
    (9, "online-news-popularity", 332, "Online News Popularity",
     "one article published on a news website: 58 features of its text and timing, and the number of times it was shared",
     lambda m: every(uci_csv(332).drop(columns=["url"]).rename(columns=str.strip), 2),
     "The url column was removed and every second row was kept (19,822 of 39,644)."),
    (10, "electrical-grid-stability", 471, "Electrical Grid Stability Simulated Data",
     "one simulated state of a small electrical grid with four nodes: reaction times, power, price coefficients, and a stability measure",
     lambda m: uci_csv(471).drop(columns=["stabf"]),
     "The text column stabf (stable or unstable) was removed."),
    (11, "letter-recognition", 59, "Letter Recognition",
     "one image of a capital letter: sixteen whole-number features of the image, each from 0 to 15",
     lambda m: uci_csv(59).drop(columns=["lettr"]),
     "The column that names the letter was removed."),
    (12, "pen-digits", 81, "Pen-Based Recognition of Handwritten Digits",
     "one digit written with a pen on a tablet: sixteen whole numbers from 0 to 100 that record the path of the pen",
     lambda m: uci_csv(81).drop(columns=["Class"]),
     "The class column was removed."),
    (13, "eeg-eye-state", 264, "EEG Eye State",
     "one reading of fourteen EEG electrodes on a person's head",
     lambda m: uci_csv(264).drop(columns=["eyeDetection"]),
     "The eye-state column was removed."),
    (14, "dry-bean", 602, "Dry Bean",
     "one grain of dry bean photographed by a camera: sixteen measurements of its size and shape",
     lambda m: uci_csv(602).drop(columns=["Class"]),
     "The class column was removed."),
    (15, "skin-segmentation", 229, "Skin Segmentation",
     "one pixel sampled from a photograph: its blue, green and red values",
     lambda m: uci_csv(229).drop(columns=["y"]),
     "The class column y was removed."),
    (16, "landsat-satellite", 146, "Statlog (Landsat Satellite)",
     "one 3 by 3 block of pixels in a satellite image: 36 brightness values, four spectral bands for each pixel",
     lambda m: uci_csv(146).drop(columns=["class"]),
     "The class column was removed."),
    (17, "spambase", 94, "Spambase",
     "one email: how often 48 words and 6 characters occur in it, and three measurements of its runs of capital letters",
     lambda m: uci_csv(94).drop(columns=["Class"]),
     "The class column was removed."),
    (18, "musk-molecules", 75, "Musk (Version 2)",
     "one shape that a molecule can take: 166 whole-number features that describe the shape",
     lambda m: uci_csv(75).drop(columns=["molecule_name", "conformation_name", "class"]),
     "The two name columns and the class column were removed."),
    (19, "credit-card-clients", 350, "Default of Credit Card Clients",
     "one credit card client: credit limit, age and three coded attributes, then six months of payment status, bill amounts and payments",
     credit,
     "The ID column and the class column Y were removed, and columns X1 to X23 were renamed to the names given in the repository's variable table."),
    (20, "metro-traffic", 492, "Metro Interstate Traffic Volume",
     "one hour on an interstate highway, 2012 to 2018: temperature, rain, snow, cloud cover, and the number of vehicles",
     lambda m: uci_csv(492).select_dtypes("number"),
     "The text columns (holiday, weather description, date and time) were removed."),
    (21, "tetouan-power", 849, "Power Consumption of Tetouan City",
     "one ten-minute reading in a city: temperature, humidity, wind speed, two solar measurements, and the power drawn by three distribution networks",
     lambda m: uci_csv(849).drop(columns=["DateTime"]),
     "The date and time column was removed."),
    (22, "steel-industry-energy", 851, "Steel Industry Energy Consumption",
     "one fifteen-minute reading at a steel plant: energy used, reactive power, carbon dioxide, power factors, and seconds since midnight",
     lambda m: uci_csv(851).select_dtypes("number"),
     "The date column and three text columns were removed."),
    (23, "room-occupancy", 864, "Room Occupancy Estimation",
     "one reading of the sensors in a room: temperature, light, sound, carbon dioxide and motion, and the number of people in the room",
     lambda m: uci_csv(864).drop(columns=["Date", "Time"]),
     "The date and time columns were removed."),
    (24, "forest-covertype", 31, "Covertype",
     "one 30-metre square of forest: elevation, slope, direction of the slope, distances to water, roads and fire points, and shade at three times of day",
     lambda m: every(uci_csv(31).iloc[:, :10], 6),
     "Only the ten quantitative columns were kept (the 44 indicator columns and the class column were removed), and every sixth row was kept (96,836 of 581,012)."),
    (25, "company-financial-ratios", 572, "Taiwanese Bankruptcy Prediction",
     "one company: 94 financial ratios from its accounts",
     lambda m: uci_csv(572).rename(columns=str.strip).drop(columns=["Bankrupt?", "Net Income Flag"]),
     "The class column and the column Net Income Flag, which has the same value in every row, were removed."),
    (26, "protein-structure", 265, "Physicochemical Properties of Protein Tertiary Structure",
     "one computed model of a protein's three-dimensional structure: nine physical and chemical properties, and its distance from the true structure",
     casp,
     "No change: CASP.csv as distributed."),
    (27, "gpu-kernel-performance", 440, "SGEMM GPU Kernel Performance",
     "one setting of a GPU program that multiplies two 2048 by 2048 matrices: fourteen parameters and four measured running times in milliseconds",
     sgemm,
     "Every fifth row was kept (48,320 of 241,600)."),
    (28, "fan-accelerometer", 846, "Accelerometer",
     "one reading of an accelerometer attached to a cooler fan: the weight configuration, the fan speed in percent, and the acceleration along x, y and z",
     accelerometer,
     "No change: the file as distributed."),
    (29, "beijing-air-quality", 501, "Beijing Multi-Site Air Quality",
     "one hour at one air-monitoring station in Beijing, 2013 to 2017: six pollutants, the weather, and the date and hour as numbers",
     beijing_station,
     "Only the Aotizhongxin station's file was used. The row counter, the wind-direction column (text) and the station name were removed, and so were the 3,188 hours with a missing value in the columns that remain."),
    (30, "land-cover-ndvi", 400, "Crowdsourced Mapping",
     "one area of a satellite image: its vegetation index (NDVI) on 27 dates in 2014 and 2015, and the largest of those values",
     crowdsourced,
     "Only training.csv was used, and its class column was removed."),
]


# ---------------------------------------------------------------- checks and output

def finish(df):
    """Numeric columns only, no holes, no constant column, a fresh index."""
    non_numeric = [c for c in df.columns if not pd.api.types.is_numeric_dtype(df[c])]
    if non_numeric:
        raise SystemExit(f"text columns left: {non_numeric}")
    if df.isna().any().any():
        raise SystemExit("missing values left")
    X = df.to_numpy(dtype=float)
    if not np.isfinite(X).all():
        raise SystemExit("an infinite value")
    sd = X.std(axis=0)
    if (sd == 0).any():
        raise SystemExit(f"constant columns: {list(df.columns[sd == 0])}")
    return df.reset_index(drop=True)


def citation(meta):
    who = "; ".join(meta.get("creators") or [])
    year = meta.get("year_of_dataset_creation")
    head = f"{who} ({year})." if who and year else (f"{who}." if who else (f"({year})." if year else ""))
    return f"{head} {meta['name'].strip()} [Dataset]. UCI Machine Learning Repository.".strip()


def main():
    only = {int(a) for a in sys.argv[1:]}
    OUT.mkdir(parents=True, exist_ok=True)
    rows, sources = [], []
    for number, name, uci_id, title, row_is, load, changed in SPECS:
        file = f"{number:02d}-{name}.csv"
        path = OUT / file
        meta = metadata(uci_id)
        lic = licence(uci_id, meta)
        if not only or number in only or not path.exists():
            df = finish(load(meta))
            df.to_csv(path, index=False, lineterminator="\n")
        else:
            df = pd.read_csv(path)
        n, m = df.shape
        size = path.stat().st_size / 1e6
        print(f"{number:2d} {file:38s} {n:7,d} x {m:3d} = {n*m:9,d} cells  {size:5.1f} MB")
        doi = f"https://doi.org/{meta['dataset_doi']}"
        rows.append(dict(number=number, file=file, title=title, rows=n, columns=m, cells=n * m,
                         megabytes=round(size, 1), one_row_is=row_is, source=doi))
        sources.append((number, file, title, meta, lic, doi, changed, n, m))

    pd.DataFrame(rows).to_csv(OUT / "datasets.csv", index=False, lineterminator="\n")

    lines = [
        "# Sources of the Unit II datasets",
        "",
        "Every file in this folder was made from a dataset of the",
        "[UCI Machine Learning Repository](https://archive.ics.uci.edu) by",
        "`tools/build_unit2_datasets.py`. Each source is licensed under the licence",
        "named in its entry, which permits sharing and adapting the data when credit",
        "is given and changes are stated. The entries below give that credit and",
        "state the changes.",
        "",
        "In every file the columns are numeric, no value is missing, and no column",
        "is constant. Values were not rescaled or rounded.",
        "",
    ]
    for number, file, title, meta, lic, doi, changed, n, m in sources:
        lines += [
            f"## {number}. {title}",
            "",
            f"- **File:** `{file}` ({n:,} rows, {m} columns)",
            f"- **Source:** {citation(meta)} <{doi}>",
            f"- **Repository page:** <{meta['repository_url']}>",
            f"- **Licence:** {lic}",
            f"- **Changes:** {changed}",
            "",
        ]
    (OUT / "SOURCES.md").write_text("\n".join(lines), encoding="utf-8", newline="\n")
    total = sum(r["megabytes"] for r in rows)
    print(f"{len(rows)} datasets, {total:.0f} MB in all")


if __name__ == "__main__":
    main()
