# Unit III · Learning algorithms

## Meeting 1 (course meeting 21) · Models, data, and validation

- [Interactive lecture](slides/m21-data-validation.html)
- [Accessible course notes · November 4, 2026](notes/meeting-21.html) · [PDF](notes/meeting-21.pdf)
- [Optional notebook](notebooks/meeting-21-data-validation.ipynb)
- [Data and attribution](data/SOURCES.md)

Download the lecture to use it offline. The notebook contains its data and runs in Python with NumPy, pandas, matplotlib, and scikit-learn. The notebook is an optional resource for exploring the examples further. The closing classroom activity is a paper review supplied by the instructor.

## Meeting 2 (course meeting 22) · Neural machines

- [Accessible course notes](notes/meeting-22.html) · [PDF](notes/meeting-22.pdf)
- [Open the companion notebook in Colab](https://colab.research.google.com/github/ikoutis/cs301-labs/blob/main/unit-3/notebooks/meeting-22-neural-machines.ipynb)
- [Notebook source and saved outputs](notebooks/meeting-22-neural-machines.ipynb)

The notebook follows the lecture: fit/predict, a tiny forward/backward/update example, downhill search and local minima, batches, sigmoid/ReLU comparisons, random-label memorization, noisy regression and validation checkpoints, and a short PyTorch training/inference loop. All datasets are generated in the notebook. The measured scikit-learn experiments use seed 22; the notebook runs on CPU without external data downloads. The moons test set remains reserved.

## Meeting 3 (course meeting 23) · Memory, similarity, and search

- [Interactive lecture](slides/m23-memory-and-retrieval.html)
- [Open the companion notebook in Colab](https://colab.research.google.com/github/ikoutis/cs301-labs/blob/main/unit-3/notebooks/meeting-23-memory-and-retrieval.ipynb)
- [Notebook source and saved outputs](notebooks/meeting-23-memory-and-retrieval.ipynb)

Explore retrieval through audio fingerprints and word embeddings, then use
k-nearest neighbors for classification and regression. Build a kd-tree one
partition at a time, step through exact search and pruning, and compare the
cost of search across dimensions. The notebook includes synthetic audio,
executed experiments, exercises, and an embedded word-vector subset; its main
route runs on CPU without external data downloads.

The lecture also lets you compare construction costs, count search work, explore
when an index repays its build cost, inspect projected word neighbors, and move
a distant neighbor to see how its prediction weight changes.
[Original November 16 lecture](slides/m23-memory-and-retrieval-2026-11-16.html)
remains available for annotations saved on that version.
