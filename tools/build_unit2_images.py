"""Build the thirty images of CS 301, Unit II.

Fifteen are paintings and prints that the Art Institute of Chicago has released
under CC0; fifteen are photographs from the NASA Image and Video Library. The
script downloads each source image once into raw/images/ (not committed),
resizes it so that its longer side is 640 pixels, and writes

    unit-2/images/NN-<name>.png        the colour image: height x width x 3
    unit-2/images/NN-<name>-grey.png   the same image in grey: height x width
    unit-2/images/images.csv           the list the notebooks read
    unit-2/images/SOURCES.md           where each image comes from, and its licence

The grey image is Pillow's conversion "L": 0.299 red + 0.587 green + 0.114 blue,
rounded to a whole number from 0 to 255.

Run from the repository root:  python tools/build_unit2_images.py
"""
import io
import json
import pathlib
import urllib.request

from PIL import Image

ROOT = pathlib.Path(__file__).resolve().parent.parent
RAW = ROOT / "raw" / "images"
OUT = ROOT / "unit-2" / "images"
LONG_SIDE = 640
UA = {"User-Agent": "Mozilla/5.0 (course material preparation)",
      "AIC-User-Agent": "CS 301 course materials, NJIT (ikoutis@njit.edu)"}

AIC_LICENCE = "CC0 1.0 Public Domain Designation (Art Institute of Chicago, open access)"
NASA_LICENCE = "Not subject to copyright in the United States (NASA images and media usage guidelines)"
NASA_GUIDELINES = "https://www.nasa.gov/nasa-brand-center/images-and-media/"

# number, file name, source, id at the source, short title (None: the source's own title)
SPECS = [
    (1, "seurat-grande-jatte", "aic", 27992, None),
    (2, "blue-marble", "nasa", "GSFC_20171208_Archive_e001788", "Earth, Eastern Hemisphere (Blue Marble 2012)"),
    (3, "monet-water-lilies", "aic", 16568, None),
    (4, "earthset-from-orion", "nasa", "art002e021278", "Earthset from the Orion Spacecraft"),
    (5, "monet-water-lily-pond", "aic", 87088, None),
    (6, "pillars-of-creation", "nasa", "GSFC_20171208_Archive_e000842", "Pillars of Creation in Near-Infrared Light (Hubble)"),
    (7, "van-gogh-bedroom", "aic", 28560, None),
    (8, "cosmic-cliffs", "nasa", "carina_nebula", "Cosmic Cliffs in the Carina Nebula (Webb)"),
    (9, "van-gogh-self-portrait", "aic", 80607, None),
    (10, "curiosity-selfie", "nasa", "PIA24173", "Curiosity's Selfie on Mars"),
    (11, "caillebotte-paris-street", "aic", 20684, None),
    (12, "aurora-from-orbit", "nasa", "iss058e005282", "Aurora over Earth, from the Space Station"),
    (13, "hokusai-great-wave", "aic", 24645, "Under the Wave off Kanagawa (The Great Wave)"),
    (14, "hurricane-helene", "nasa", "iss072e001649", "Hurricane Helene, from the Space Station"),
    (15, "cezanne-basket-of-apples", "aic", 111436, None),
    (16, "bahama-islands-1983", "nasa", "s06-45-097", "Bahama Islands, from the Space Shuttle"),
    (17, "van-gogh-fruit", "aic", 64957, None),
    (18, "bahamas-2024", "nasa", "iss071e449837", "The Bahamas, from the Space Station"),
    (19, "renoir-two-sisters", "aic", 14655, None),
    (20, "crab-nebula", "nasa", "PIA03606", "The Crab Nebula (Hubble)"),
    (21, "monet-stacks-of-wheat", "aic", 64818, None),
    (22, "sun", "nasa", "PIA26681", "The Sun (Solar Dynamics Observatory)"),
    (23, "homer-herring-net", "aic", 25865, None),
    (24, "helix-nebula-ultraviolet", "nasa", "PIA15658", "The Helix Nebula in Ultraviolet Light (GALEX)"),
    (25, "hiroshige-hamamatsu", "aic", 4371, "Hamamatsu, from Fifty-three Stations of the Tokaido"),
    (26, "helix-nebula-infrared", "nasa", "PIA09178", "The Helix Nebula in Infrared Light (Spitzer)"),
    (27, "hiroshige-mitsuke", "aic", 4368, "Mitsuke: Ferries Crossing the Tenryu River"),
    (28, "astronaut-spacewalk", "nasa", "iss059e002710", "An Astronaut's Self-Portrait on a Spacewalk"),
    (29, "monet-houses-of-parliament", "aic", 16584, None),
    (30, "shuttle-endeavour", "nasa", "201002060005HQ", "Space Shuttle Endeavour on the Launch Pad"),
]


def get(url):
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=120) as r:
        return r.read()


def cached(url, dest):
    if not (dest.exists() and dest.stat().st_size > 0):
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_bytes(get(url))
    return dest.read_bytes()


def from_aic(art_id):
    fields = "id,title,artist_title,date_display,image_id,is_public_domain"
    a = json.loads(cached(f"https://api.artic.edu/api/v1/artworks/{art_id}?fields={fields}", RAW / f"aic-{art_id}.json"))["data"]
    if not a["is_public_domain"]:
        raise SystemExit(f"AIC {art_id} is not marked public domain")
    data = cached(f"https://www.artic.edu/iiif/2/{a['image_id']}/full/843,/0/default.jpg", RAW / f"aic-{art_id}.jpg")
    return data, dict(title=a["title"], creator=a["artist_title"], date=a["date_display"],
                      source=f"https://www.artic.edu/artworks/{art_id}", licence=AIC_LICENCE,
                      holder="Art Institute of Chicago")


def from_nasa(nasa_id):
    meta = json.loads(cached(f"https://images-api.nasa.gov/search?nasa_id={nasa_id}", RAW / f"nasa-{nasa_id}.json"))
    d = meta["collection"]["items"][0]["data"][0]
    assets = json.loads(cached(f"https://images-api.nasa.gov/asset/{nasa_id}", RAW / f"nasa-{nasa_id}-assets.json"))
    hrefs = [i["href"] for i in assets["collection"]["items"]]
    for size in ("~medium.jpg", "~large.jpg", "~small.jpg"):
        url = next((h for h in hrefs if h.endswith(size)), None)
        if url:
            try:
                data = cached(url.replace("http://", "https://"), RAW / f"nasa-{nasa_id}{size.replace('~', '-')}")
                break
            except Exception:  # noqa: BLE001  some sizes answer 403
                continue
    else:
        raise SystemExit(f"no image found for NASA {nasa_id}")
    credit = d.get("secondary_creator") or d.get("photographer") or f"NASA/{d.get('center', '')}".rstrip("/")
    if "NASA" not in credit:
        credit = "NASA/" + credit
    # the library dates its "GSFC_20171208_Archive" records by the day they were archived, not by the image
    date = "" if nasa_id.startswith("GSFC_20171208_Archive") else (d.get("date_created") or "")[:4]
    return data, dict(title=d["title"].strip(), creator=credit, date=date,
                      source=f"https://images.nasa.gov/details/{nasa_id}", licence=NASA_LICENCE,
                      holder="NASA Image and Video Library")


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    rows, lines = [], [
        "# Sources of the Unit II images",
        "",
        "Every image in this folder was made by `tools/build_unit2_images.py`: the source",
        "image was resized so that its longer side is 640 pixels and saved as a PNG file,",
        "once in colour and once in grey. Nothing else was changed.",
        "",
        "- Images from the **Art Institute of Chicago** are works that the museum has",
        "  released into the public domain under CC0 1.0.",
        "- Images from the **NASA Image and Video Library** follow NASA's",
        f"  [images and media usage guidelines]({NASA_GUIDELINES}): NASA content is",
        "  generally not subject to copyright in the United States and may be used for",
        "  educational purposes. The credit given by the library is repeated below.",
        "  Their use here does not imply any endorsement by NASA.",
        "",
    ]
    for number, name, kind, source_id, short in SPECS:
        data, info = (from_aic if kind == "aic" else from_nasa)(source_id)
        img = Image.open(io.BytesIO(data)).convert("RGB")
        scale = LONG_SIDE / max(img.size)
        img = img.resize((round(img.width * scale), round(img.height * scale)), Image.LANCZOS)
        file, grey_file = f"{number:02d}-{name}.png", f"{number:02d}-{name}-grey.png"
        img.save(OUT / file, optimize=True)
        img.convert("L").save(OUT / grey_file, optimize=True)
        title = short or info["title"]
        kb = ((OUT / file).stat().st_size + (OUT / grey_file).stat().st_size) / 1e3
        print(f"{number:2d} {file:36s} {img.height:4d} x {img.width:4d}  {kb:6.0f} kB  {title} | {info['creator']} | {info['date']}")
        rows.append(dict(number=number, file=file, grey_file=grey_file, title=title, creator=info["creator"],
                         date=info["date"], height=img.height, width=img.width, source=info["source"]))
        lines += [
            f"## {number}. {title}",
            "",
            f"- **Files:** `{file}`, `{grey_file}` ({img.height} by {img.width} pixels)",
            f"- **Original title:** {info['title']}",
            f"- **Creator or credit:** {info['creator']}" + (f", {info['date']}" if info["date"] else ""),
            f"- **Source:** {info['holder']}, <{info['source']}>",
            f"- **Licence:** {info['licence']}",
            "",
        ]
    import csv
    with open(OUT / "images.csv", "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0]), lineterminator="\n")
        w.writeheader()
        w.writerows(rows)
    (OUT / "SOURCES.md").write_text("\n".join(lines), encoding="utf-8", newline="\n")
    total = sum(p.stat().st_size for p in OUT.glob("*.png")) / 1e6
    print(f"{len(rows)} images, {total:.1f} MB in all")


if __name__ == "__main__":
    main()
