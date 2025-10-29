from __future__ import annotations

from typing import Literal


def detect_intent(query: str) -> Literal["lookup", "comparison", "tutorial", "solution-seeking"]:
    q = query.lower()
    if any(k in q for k in [" vs ", "compare", "versus"]):
        return "comparison"
    if any(k in q for k in ["how to", "tutorial", "guide"]):
        return "tutorial"
    if any(k in q for k in ["best", "top", "which"]):
        return "solution-seeking"
    return "lookup"
