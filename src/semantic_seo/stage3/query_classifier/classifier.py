from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from semantic_seo.stage2.conversational_query_extraction.extractor import extract_from_prompt


@dataclass
class QueryClassification:
    entity: Optional[str]
    intent: str
    micro_intent: str


def classify_query(query: str) -> QueryClassification:
    """Simple baseline classifier using heuristics; replace with ML later."""
    extracted = extract_from_prompt(query)
    micro = "comparison" if "comparison" in extracted.get("intents", []) else "quick-lookup"
    intent = "solution-seeking" if micro != "comparison" else "research"
    entity = (extracted.get("entities") or [None])[0]
    return QueryClassification(entity=entity, intent=intent, micro_intent=micro)
