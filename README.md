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
  `m15-essentials.html` (meeting 15, part 1: the must-knows of Unit II) is a
  review in which every picture is drawn step by step: the space bar, or a
  click on the picture, runs the next step; it has no PDF. `m16-svd.html`
  (meeting 16: the dimensionality of data, the SVD told from a cloud of
  points) is drawn the same way, with sliders for the flatness of a cloud
  and the direction of a projection, and a cloud in space that turns; no PDF.
- `unit-2/assignments/`: the notebooks of the Unit II assignments, opened in Colab
  from here: `vectorization.ipynb` (Homework 1) and the four practice notebooks
  of Assignment 2, `01-comparing-data`, `02-neurons-and-arrays`,
  `03-cost-and-hardware` and `04-systems-and-sparsity`, which practise the
  essentials of meetings 10 to 14 with predictions, checked exercises and
  explanations. The [image-segmentation mini-project](https://colab.research.google.com/github/ikoutis/cs301-labs/blob/main/unit-2/assignments/image-segmentation.ipynb)
  builds 4- and 8-neighbor affinity graphs, compares Python and Numba loops,
  constructs dense and sparse Laplacians, and solves seeded segmentation
  systems. It includes a Colab seed picker, saved-seed replay, runtime and
  memory comparisons, reflection prompts, and an optional multiclass extension.
- `unit-2/notes/`: the notes of the meetings, one web page for each meeting
  (`meeting-10.html`), with the same page as a PDF beside it. The notes state
  the main points of the meeting first and then walk through its notebooks step
  by step; the code of every step, with the output it produced for one group,
  opens under the prose. Built from the notebooks in the course repository;
  `fonts/` holds the fonts the pages use.
- `unit-2/pages/`: web pages that a meeting uses in place of slides. Each is one
  self-contained HTML file.
  - `cpu-and-gpu.html` (meeting 11): the two processors, and how a product of
    matrices is divided on each.
  - `matrix-costs.html` (meeting 11): the number of operations behind each matrix
    operation of the lab, and a calculator that turns a count into a time.
  - `random-walk.html` (meeting 13): the random walk of the first notebook, animated on
    the notebook's own graph: one walker step by step, or a thousand at once, and the
    fraction that reaches red first under every node; the exact answer, a linear
    system, behind a button.
  - `linear-systems.html` (meeting 13): moving pictures of the notions of the first
    notebook and of elimination: two lines and their crossing, nearly parallel lines
    and the condition number, three planes that turn, and elimination as planes that
    pivot while the solution stays.
  - `solvers-and-sparse.html` (meeting 13): the three ways to solve a system racing on
    a Colab clock, with repeated runs; the residual against the error as a band of
    near-solutions that stretches as two lines close up; and the sparse formats on the
    3 x 3 grid's matrix, built entry by entry, with a product that counts the
    multiplications by zero.
  - `correlation.html` (meeting 14): the correlation coefficient as the average
    product of two standardized columns, on real pairs of features of the movies;
    and the correlation matrix of the 19 genres built cell by cell, then ordered
    so that blocks appear.
  - `two-products.html` (meeting 14): the same matrix multiplied two ways, on a
    small matrix of people by genres and on the has-rated matrix of 610 people by
    1,297 movies, computed on the page; one movie under three definitions of
    similar; forty movies in one picture; and the size of the two products of the
    word vectors.
  - `axes.html` (Act 3 of meeting 14, not taught there; moved to meeting 15): a line that turns through a cloud of 1,297 movies
    and finds the direction of greatest spread; the two axes and the ellipse; the
    cloud flattened until the matrix loses rank; the 19 genres by their weights in
    the first two components, with a copied column; and a map of 50 movies.
  - `correlation-slides.html` and `two-products-slides.html` (meeting 14), and
    `axes-slides.html` (meeting 15): the same three pages as slides for the projector, 1280 by 720
    scaled to the window: one tab a slide, with its controls and readouts in
    larger type beside the picture, followed by a slide with the tab's points.
    The arrow keys turn the slides, F fills the screen, and the address can name
    a slide (`axes-slides.html#6`).
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
- `unit-2/movies/`: the MovieLens small dataset of GroupLens Research, 100,836
  ratings of 9,742 movies by 610 people (`ratings.csv`, `movies.csv`, `tags.csv`),
  with the dataset's own `README.txt`, which holds its usage license, and
  `SOURCES.md`. For research use, not for commercial use; see the license.
- `tools/build_unit2_datasets.py`, `tools/build_unit2_images.py`,
  `tools/build_unit2_embeddings.py` and `tools/build_unit2_movies.py`: the scripts
  that built the datasets, the images, the word vectors and the movie ratings from
  their sources.

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
