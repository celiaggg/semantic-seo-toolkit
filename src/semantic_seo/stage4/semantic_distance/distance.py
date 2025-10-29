from __future__ import annotations

from typing import Iterable, List

import numpy as np


def cosine_similarity(vec_a: Iterable[float], vec_b: Iterable[float]) -> float:
    a = np.array(list(vec_a), dtype=float)
    b = np.array(list(vec_b), dtype=float)
    denom = np.linalg.norm(a) * np.linalg.norm(b)
    if denom == 0:
        return 0.0
    return float(np.dot(a, b) / denom)


def pairwise_cosine_matrix(vectors: List[List[float]]) -> List[List[float]]:
    n = len(vectors)
    mat = [[0.0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(i, n):
            sim = cosine_similarity(vectors[i], vectors[j])
            mat[i][j] = sim
            mat[j][i] = sim
    return mat
