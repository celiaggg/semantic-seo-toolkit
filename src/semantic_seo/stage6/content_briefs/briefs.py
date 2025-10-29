from __future__ import annotations

from typing import Dict, List

from semantic_seo.stage3.micro_intent_mapping.mapper import map_to_content_format


def generate_brief(topic: str, micro_intent: str, required_entities: List[str]) -> Dict[str, object]:
    """Produce a simple content brief structure for a topic and micro-intent."""
    content_format = map_to_content_format(micro_intent)  # type: ignore[arg-type]
    outline = [
        "Introduction",
        f"{topic} overview",
        "Key entities and concepts",
        "Examples / Code snippets",
        "FAQ",
    ]
    return {
        "topic": topic,
        "format": content_format,
        "entities": required_entities,
        "outline": outline,
        "notes": [
            "Use concise, semantically dense paragraphs",
            "Link to related entities in the site map",
        ],
    }
