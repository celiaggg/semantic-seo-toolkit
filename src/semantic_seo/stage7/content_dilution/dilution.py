from __future__ import annotations

from typing import Iterable, List


def find_diluted_pages(pages: Iterable[str], *, core_terms: Iterable[str]) -> List[int]:
    """Return indices of pages that do not mention any core terms."""
    terms = [t.lower() for t in core_terms]
    diluted: List[int] = []
    for i, page in enumerate(pages):
        lower = page.lower()
        if not any(t in lower for t in terms):
            diluted.append(i)
    return diluted
