# Source of the Unit II movie ratings

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
- **Changes:** none to the content. The files are copies of those in the zip; the
  repository stores them with Unix line endings, which the zip's files do not all
  have.

This copy is course material of CS 301 at NJIT and is not endorsed by the
University of Minnesota or by GroupLens Research.
