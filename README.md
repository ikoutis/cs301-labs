# CS 301 labs

Lab notebooks and datasets for **CS 301, Introduction to Data Science**, at the
New Jersey Institute of Technology. The notebooks open in Google Colab and read
the datasets from this repository's public site,
<https://ikoutis.github.io/cs301-labs/>.

## Contents

- `unit-2/notebooks/`: one notebook for each meeting of Unit II.
- `unit-2/data/`: thirty tabular datasets, numbered 1 to 30.
  - `datasets.csv` lists them: number, file, title, size, and what one row is.
  - `SOURCES.md` gives the source and the licence of each dataset, and states
    what was changed.
- `unit-2/images/`: thirty images, numbered 1 to 30, each as a colour PNG file and
  as a grey PNG file, with the longer side 640 pixels.
  - `images.csv` lists them: number, files, title, creator, size, source.
  - `SOURCES.md` gives the source and the licence of each image.
- `tools/build_unit2_datasets.py` and `tools/build_unit2_images.py`: the scripts
  that built the datasets and the images from their sources.

## The datasets

Every file is a CSV file with a header line. All columns are numeric, no value
is missing, and no column is constant. The files hold between 130,000 and
1,200,000 numbers each.

To read one in Python:

```python
import pandas as pd

BASE = "https://ikoutis.github.io/cs301-labs/unit-2/data/"
datasets = pd.read_csv(BASE + "datasets.csv", index_col="number")
df = pd.read_csv(BASE + datasets.loc[7, "file"])
```

## Licence of the data and the images

The datasets come from the
[UCI Machine Learning Repository](https://archive.ics.uci.edu) and are licensed
under the Creative Commons Attribution 4.0 International licence (CC BY 4.0).
`unit-2/data/SOURCES.md` credits each one. If you reuse a file, credit its
source in the same way.

Fifteen images are works that the Art Institute of Chicago has released under
CC0 1.0. Fifteen are from the NASA Image and Video Library and follow NASA's
images and media usage guidelines. `unit-2/images/SOURCES.md` gives the source
and the credit of each one.
