"""Build the movie ratings data of CS 301, Unit II (meeting 14).

The data is the MovieLens "ml-latest-small" dataset of GroupLens Research at the
University of Minnesota: 100,836 ratings and 3,683 tag applications across
9,742 movies by 610 users, generated 2018-09-26. The script downloads the zip
once into raw/ (not committed) and writes, unchanged,

    unit-2/movies/ratings.csv    userId, movieId, rating, timestamp
    unit-2/movies/movies.csv     movieId, title, genres
    unit-2/movies/tags.csv       userId, movieId, tag, timestamp
    unit-2/movies/README.txt     the dataset's own README, with its usage license, verbatim
    unit-2/movies/SOURCES.md     where the files come from, the licence, what was changed (nothing)

The usage license of the dataset permits redistribution, including
transformations, under the same conditions: no implied endorsement, an
acknowledgement in publications, and no commercial use without permission.
The README.txt kept beside the files states those conditions in full.

Run from the repository root:

    python tools/build_unit2_movies.py
"""
import io
import pathlib
import urllib.request
import zipfile

ROOT = pathlib.Path(__file__).resolve().parent.parent
RAW = ROOT / "raw"
OUT = ROOT / "unit-2" / "movies"
URL = "https://files.grouplens.org/datasets/movielens/ml-latest-small.zip"
KEEP = ["ratings.csv", "movies.csv", "tags.csv", "README.txt"]
UA = {"User-Agent": "Mozilla/5.0 (course material preparation)"}

SOURCES = """# Source of the Unit II movie ratings

The files in this folder were copied, unchanged, by `tools/build_unit2_movies.py`
from the MovieLens dataset `ml-latest-small` of GroupLens Research, University of
Minnesota.

- **Source:** <https://grouplens.org/datasets/movielens/latest/>, the file
  `ml-latest-small.zip`, generated on September 26, 2018: 100,836 ratings and 3,683
  tag applications across 9,742 movies, by 610 users who each rated at least 20
  movies, between March 29, 1996 and September 24, 2018. The users were selected at
  random; no demographic information is included.
- **Citation:** F. Maxwell Harper and Joseph A. Konstan. 2015. The MovieLens
  Datasets: History and Context. ACM Transactions on Interactive Intelligent
  Systems (TiiS) 5, 4, Article 19 (December 2015). <https://doi.org/10.1145/2827872>
- **Licence:** the dataset's usage license, reproduced in full in `README.txt`
  beside this file. In short: the data may be used for research purposes; the user
  may not state or imply any endorsement from the University of Minnesota or the
  GroupLens Research Group; the use of the data set must be acknowledged in
  publications; the data may be redistributed, including transformations, under
  these same conditions; it may not be used for commercial or revenue-bearing
  purposes without permission from a faculty member of the GroupLens Research
  Project. Neither the University of Minnesota nor the researchers involved
  guarantee the correctness of the data or its suitability for any purpose.
- **Files:** `ratings.csv` (userId, movieId, rating, timestamp), `movies.csv`
  (movieId, title, genres, with the genres separated by `|`), `tags.csv` (userId,
  movieId, tag, timestamp). `links.csv` of the original is not included.
- **Changes:** none. The files are byte-for-byte copies of those in the zip.

This copy is course material of CS 301 at NJIT and is not endorsed by the
University of Minnesota or by GroupLens Research.
"""


def fetch(url, dest):
    """Download url to dest unless a non-empty copy is already there."""
    if dest.exists() and dest.stat().st_size > 0:
        return dest
    dest.parent.mkdir(parents=True, exist_ok=True)
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=300) as r, open(dest, "wb") as f:
        f.write(r.read())
    return dest


def main():
    zip_path = fetch(URL, RAW / "ml-latest-small.zip")
    OUT.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(zip_path) as z:
        names = {pathlib.PurePosixPath(n).name: n for n in z.namelist()}
        for name in KEEP:
            data = z.read(names[name])
            (OUT / name).write_bytes(data)
            print(f"wrote {OUT / name} ({len(data):,} bytes)")
    (OUT / "SOURCES.md").write_text(SOURCES, encoding="utf-8")
    print(f"wrote {OUT / 'SOURCES.md'}")


if __name__ == "__main__":
    main()
