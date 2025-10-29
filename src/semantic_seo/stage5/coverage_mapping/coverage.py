from __future__ import annotations

from typing import Dict, Iterable, List


def map_queries_to_content(queries: Iterable[str], contents: Iterable[str]) -> Dict[str, List[int]]:
    """Naive coverage mapping by substring containment.

    Returns a dict mapping each query to a list of indices of matching contents.
    """
    q_list = list(queries)
    c_list = list(contents)
    mapping: Dict[str, List[int]] = {}
    for i, q in enumerate(q_list):
        matches: List[int] = []
        for j, c in enumerate(c_list):
            if q.lower() in c.lower():
                matches.append(j)
        mapping[q] = matches
    return mapping
