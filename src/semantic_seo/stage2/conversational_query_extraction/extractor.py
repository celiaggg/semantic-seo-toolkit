from __future__ import annotations

from typing import Dict, List

from semantic_seo.shared.utils.text import normalize_whitespace


def extract_from_prompt(prompt: str) -> Dict[str, List[str]]:
    """Naive conversational query element extraction.

    Returns a dict with lists for entities, attributes, intents, questions.
    """
    clean = normalize_whitespace(prompt.lower())
    # Extremely simple heuristics
    intents: List[str] = []
    if any(x in clean for x in ["compare", "vs", "versus"]):
        intents.append("comparison")
    if any(x in clean for x in ["how to", "tutorial", "guide"]):
        intents.append("how-to")
    if any(x in clean for x in ["latency", "scalability", "cost"]):
        attributes = [w for w in ["latency", "scalability", "cost"] if w in clean]
    else:
        attributes = []
    # Entities left to downstream NER / embedding matching
    return {"entities": [], "attributes": attributes, "intents": intents, "questions": []}
