from __future__ import annotations

from typing import Literal


def map_to_content_format(intent: Literal["lookup", "comparison", "tutorial", "solution-seeking"]) -> str:
    if intent == "comparison":
        return "comparison-table"
    if intent == "tutorial":
        return "how-to-guide"
    if intent == "solution-seeking":
        return "solution-overview"
    return "reference-snippet"
