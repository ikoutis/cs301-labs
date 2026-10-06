# CS 301 labs

Lab notebooks and datasets for **CS 301, Introduction to Data Science**, at the
New Jersey Institute of Technology. The notebooks open in Google Colab and read
the datasets from this repository's public site,
<https://ikoutis.github.io/cs301-labs/>.

## Contents

- `unit-2/notebooks/`: the notebooks of Unit II. A meeting has one **class
  notebook** (`meeting-10-class.ipynb`), with the short Colab blocks that the
  groups run in class after the slides of each act, and one **full notebook**
  for each act (`meeting-10-act-1.ipynb`, ...), which explains every step and
  holds the work for after the meeting. Each runs on its own.
- `unit-2/slides/`: the slide decks of the meetings, one web page for each act
  (`m10-act-1.html`, ...), self-contained, built from the full notebooks: the
  code is shown with the output it produced for one group. The arrow keys turn
  the slides; the address can name a slide (`m10-act-1.html#9`); the button at
  the bottom right stacks all the slides on one page, for reading. Beside each
  page is the same deck as a PDF (`m10-act-1.pdf`), one page for each slide.
- `unit-2/pages/`: web pages that a meeting uses in place of slides. Each is one
  self-contained HTML file.
  - `cpu-and-gpu.html` (meeting 11): the two processors, and how a product of
    matrices is divided on each.
  - `matrix-costs.html` (meeting 11): the number of operations behind each matrix
    operation of the lab, and a calculator that turns a count into a time.
- `unit-2/data/`: thirty tabular datasets, numbered 1 to 30.
  - `datasets.csv` lists them: number, file, title, size, and what one row is.
  - `SOURCES.md` gives the source and the licence of each dataset, and states
    what was changed.
- `unit-2/images/`: thirty images, numbered 1 to 30, each as a colour PNG file and
  as a grey PNG file, with the longer side 640 pixels.
  - `images.csv` lists them: number, files, title, creator, size, source.
  - `SOURCES.md` gives the source and the licence of each image.
- `unit-2/embeddings/`: word vectors for 50,000 English words, with 50 and with 300
  numbers for each word (`words.txt`, `glove-50.npy`, `glove-300.npy`).
  - `SOURCES.md` gives their source and licence.
- `unit-2/weather/`: the daily weather at Newark airport from 2006 to 2024
  (`newark-weather.csv`), with `SOURCES.md`.
- `tools/build_unit2_datasets.py`, `tools/build_unit2_images.py` and
  `tools/build_unit2_embeddings.py`: the scripts that built the datasets, the
  images and the word vectors from their sources.

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

## Licence of the data, the images and the word vectors

The datasets come from the
[UCI Machine Learning Repository](https://archive.ics.uci.edu) and are licensed
under the Creative Commons Attribution 4.0 International licence (CC BY 4.0).
`unit-2/data/SOURCES.md` credits each one. If you reuse a file, credit its
source in the same way.

Fifteen images are works that the Art Institute of Chicago has released under
CC0 1.0. Fifteen are from the NASA Image and Video Library and follow NASA's
images and media usage guidelines. `unit-2/images/SOURCES.md` gives the source
and the credit of each one.

The word vectors are a part of the GloVe vectors of the Stanford NLP Group, which
are made available under the Public Domain Dedication and License v1.0.
`unit-2/embeddings/SOURCES.md` gives the source and states what was changed.

The weather data is from NOAA's Global Historical Climatology Network Daily, a
work of the United States government in the public domain.
`unit-2/weather/SOURCES.md` gives the source and states what was changed.
