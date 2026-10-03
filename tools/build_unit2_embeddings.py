"""Build the word vectors of CS 301, Unit II, from the GloVe vectors of Stanford NLP.

Source: glove.6B.zip (Wikipedia 2014 + Gigaword 5, 400,000 lower-case words), which
holds one text file for each dimension. The pre-trained vectors are made available
under the Public Domain Dedication and License v1.0. The script downloads the zip
once into raw/glove/ (862 MB, not committed) and writes

    unit-2/embeddings/words.txt       50,000 words, one per line, most frequent first
    unit-2/embeddings/glove-50.npy    their vectors with 50 numbers each, 50,000 x 50
    unit-2/embeddings/glove-300.npy   their vectors with 300 numbers each, 50,000 x 300
    unit-2/embeddings/SOURCES.md      the source, the licence, what was changed

The words kept are the 50,000 most frequent ones that consist of the letters a to z
only (no digits, no punctuation), without a short list of slurs and strong profanity
(BLOCKED holds hashes of those words, so that the list itself is not published).
The vectors are stored as 16-bit numbers to keep the files small; a value changes by
less than 0.001 of its size.

Run from the repository root:  python tools/build_unit2_embeddings.py
"""
import hashlib
import io
import pathlib
import re
import urllib.request
import zipfile

import numpy as np

ROOT = pathlib.Path(__file__).resolve().parent.parent
ZIP = ROOT / "raw" / "glove" / "glove.6B.zip"
OUT = ROOT / "unit-2" / "embeddings"
URL = "https://downloads.cs.stanford.edu/nlp/data/glove.6B.zip"
WORDS = 50_000
DIMENSIONS = (50, 300)
LETTERS = re.compile(r"^[a-z]+$")

BLOCKED = set("""
f50c51ed2315 26578569a290 d75a838dc758 5a9d9dcefb56 665cb762e3bc 30a989afc82c f9d0d9b18ae9 45cd3e1bb472
7c4a5c242b72 e7b98c6aa5b9 daec0c235d31 594810adcbee 566f532d486c 6556c1a58444 066e6872d931 886d51e97ad7
92a9bf818e7e 9915ba2d8222 8f5083e3e5c7 1e02eec4f109 17bde8b40646 6ac3c336e409 b690cdbe59f1 bb61ef40814c
63333e4b5d1c 31506a8448a7 cc02032349c8 82159dd02870 83621b34ec59 c3de533e9b7f 268651b3ece9 2f5f6ce5ae30
08a841e99678 341d56384afc 120f6e5b4ea3 5b3ae48be122 8c5c04391361 0033728f0fbc 0f28c4960d96 158869a97379
c1cabb6f6e43 85fc17f7069a 986c99004163 c2c3b68b4883 11cf8376a157 98b52c4b6b7d 16ea09fc78ca dd92623b0a4b
89133bc00e9b bdb1cc258d69 eef3bd091670 0ce875d62007 9ae315a94e42 937d56e49744
""".split())


def kept(word):
    return bool(LETTERS.match(word)) and hashlib.sha256(word.encode()).hexdigest()[:12] not in BLOCKED


def read(z, dimension):
    """The first WORDS kept words of one file of the zip, and their vectors."""
    words, rows = [], []
    with z.open(f"glove.6B.{dimension}d.txt") as f:
        for line in io.TextIOWrapper(f, encoding="utf-8"):
            word, _, rest = line.partition(" ")
            if kept(word):
                words.append(word)
                rows.append(np.array(rest.split(), dtype=np.float32))
                if len(words) == WORDS:
                    break
    return words, np.vstack(rows)


def main():
    if not ZIP.exists():
        ZIP.parent.mkdir(parents=True, exist_ok=True)
        print("downloading", URL)
        urllib.request.urlretrieve(URL, ZIP)
    OUT.mkdir(parents=True, exist_ok=True)
    reference = None
    with zipfile.ZipFile(ZIP) as z:
        for d in DIMENSIONS:
            words, E = read(z, d)
            assert E.shape == (WORDS, d), E.shape
            if reference is None:
                reference = words
                (OUT / "words.txt").write_text("\n".join(words) + "\n", encoding="utf-8", newline="\n")
            assert words == reference, "the files of the zip list the words in different orders"
            small = E.astype(np.float16)
            worst = float(np.abs(small.astype(np.float32) - E).max())
            np.save(OUT / f"glove-{d}.npy", small)
            mb = (OUT / f"glove-{d}.npy").stat().st_size / 1e6
            print(f"glove-{d}.npy: {E.shape[0]:,} x {E.shape[1]}, {mb:.1f} MB, largest change from 16-bit storage {worst:.5f}")
    print("first words:", " ".join(reference[:12]), "| last:", " ".join(reference[-5:]))

    (OUT / "SOURCES.md").write_text("\n".join([
        "# Source of the Unit II word vectors",
        "",
        "The files in this folder were made by `tools/build_unit2_embeddings.py` from the",
        "GloVe word vectors of the Stanford NLP Group.",
        "",
        "- **Source:** Jeffrey Pennington, Richard Socher and Christopher D. Manning (2014).",
        "  *GloVe: Global Vectors for Word Representation.* Pre-trained vectors",
        "  `glove.6B.zip`: Wikipedia 2014 and Gigaword 5, 6 billion tokens, 400,000",
        "  lower-case words. <https://nlp.stanford.edu/projects/glove/>",
        "- **Licence:** the pre-trained word vectors are made available under the Public",
        "  Domain Dedication and License v1.0,",
        "  <http://www.opendatacommons.org/licenses/pddl/1.0/>.",
        "- **Files:** `words.txt` (50,000 words, most frequent first), `glove-50.npy`",
        "  (50,000 by 50) and `glove-300.npy` (50,000 by 300). Row k of each array is the",
        "  vector of the word on line k of `words.txt`, counting from 0.",
        "- **Changes:** only the 50,000 most frequent words that consist of the letters a",
        "  to z were kept; a short list of slurs and strong profanity was left out; the",
        "  numbers are stored with 16 bits each. The vectors were not otherwise altered.",
        "",
        "The vectors were computed from a large body of text written by people. They",
        "reproduce regularities of that text, including its stereotypes.",
        "",
    ]), encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
