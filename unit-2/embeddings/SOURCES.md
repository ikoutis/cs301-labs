# Source of the Unit II word vectors

The files in this folder were made by `tools/build_unit2_embeddings.py` from the
GloVe word vectors of the Stanford NLP Group.

- **Source:** Jeffrey Pennington, Richard Socher and Christopher D. Manning (2014).
  *GloVe: Global Vectors for Word Representation.* Pre-trained vectors
  `glove.6B.zip`: Wikipedia 2014 and Gigaword 5, 6 billion tokens, 400,000
  lower-case words. <https://nlp.stanford.edu/projects/glove/>
- **Licence:** the pre-trained word vectors are made available under the Public
  Domain Dedication and License v1.0,
  <http://www.opendatacommons.org/licenses/pddl/1.0/>.
- **Files:** `words.txt` (50,000 words, most frequent first), `glove-50.npy`
  (50,000 by 50) and `glove-300.npy` (50,000 by 300). Row k of each array is the
  vector of the word on line k of `words.txt`, counting from 0.
- **Changes:** only the 50,000 most frequent words that consist of the letters a
  to z were kept; a short list of slurs and strong profanity was left out; the
  numbers are stored with 16 bits each. The vectors were not otherwise altered.

The vectors were computed from a large body of text written by people. They
reproduce regularities of that text, including its stereotypes.
