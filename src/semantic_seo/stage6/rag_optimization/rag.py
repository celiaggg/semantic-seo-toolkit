from __future__ import annotations

from typing import Dict, Iterable


def rag_readiness_check(page: str, *, required_sections: Iterable[str]) -> Dict[str, object]:
    """Check whether a page includes key RAG-friendly sections.

    Returns presence flags for each required section.
    """
    lower = page.lower()
    sections = {s: (s.lower() in lower) for s in required_sections}
    return {"sections": sections, "all_present": all(sections.values())}
