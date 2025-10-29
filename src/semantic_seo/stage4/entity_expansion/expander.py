from __future__ import annotations

from typing import Dict, Iterable, List


def expand_entities(seed_entities: Iterable[str], related_terms: Dict[str, List[str]]) -> List[str]:
    """Expand entities using a precomputed related-terms map."""
    out: List[str] = []
    for e in seed_entities:
        out.append(e)
        out.extend(related_terms.get(e, []))
    # dedupe
    seen = set()
    unique: List[str] = []
    for x in out:
        if x not in seen:
            unique.append(x)
            seen.add(x)
    return unique
