from __future__ import annotations

from collections import Counter
from typing import Dict, Iterable, List, Tuple


def cooccurrence_pairs(tokens: Iterable[str]) -> Counter[Tuple[str, str]]:
    """Return pair counts for adjacent token co-occurrences."""
    tokens_list = list(tokens)
    counts: Counter[Tuple[str, str]] = Counter()
    for a, b in zip(tokens_list, tokens_list[1:]):
        if a and b:
            key = tuple(sorted((a, b)))
            counts[key] += 1
    return counts
