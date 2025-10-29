from __future__ import annotations

from typing import Dict, List

from semantic_seo.stage0.context_modeling.contexts import DecisionContext


def extract_query_elements_from_context(context: DecisionContext) -> Dict[str, List[str]]:
    """Convert a decision context into structured query elements.

    Returns a dict with keys: entities, attributes, intents, questions (basic heuristic).
    """
    entities = []  # e.g., Elasticsearch, vector database
    attributes = context.use_case.constraints
    intents = ["solution-seeking"]
    questions = [
        f"How to implement: {context.use_case.title}?",
    ]
    return {
        "entities": entities,
        "attributes": attributes,
        "intents": intents,
        "questions": questions,
    }
