from __future__ import annotations

from typing import Iterable


def topical_focus_score(pages: Iterable[str], *, core_terms: Iterable[str]) -> float:
    """Compute a naive topical focus score in [0, 1].

    Proportion of pages that include at least one core term.
    """
    pages_list = list(pages)
    if not pages_list:
        return 0.0
    terms = [t.lower() for t in core_terms]
    covered = 0
    for p in pages_list:
        lower = p.lower()
        if any(t in lower for t in terms):
            covered += 1
    return covered / len(pages_list)
