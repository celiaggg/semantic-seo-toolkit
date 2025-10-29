from __future__ import annotations

from typing import Iterable, List

from sklearn.cluster import KMeans
from sklearn.feature_extraction.text import TfidfVectorizer


def tfidf_kmeans_clusters(texts: Iterable[str], *, n_clusters: int = 8) -> List[int]:
    """Cluster texts using TF-IDF + KMeans. Returns cluster labels per text."""
    texts_list = list(texts)
    if not texts_list:
        return []
    vect = TfidfVectorizer(max_features=5000, ngram_range=(1, 2))
    X = vect.fit_transform(texts_list)
    km = KMeans(n_clusters=n_clusters, n_init=10, random_state=42)
    labels = km.fit_predict(X)
    return list(map(int, labels))
