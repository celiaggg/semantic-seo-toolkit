from __future__ import annotations

from typing import Dict, Iterable, List, Tuple


def disambiguate_entities(candidates: Iterable[Dict[str, str]]) -> List[Dict[str, str]]:
    """Placeholder for entity disambiguation logic.

    Strategy ideas:
    - Use context windows around mentions
    - Compare to knowledge base (e.g., Elasticsearch index with canonical entities)
    - Score candidates by string similarity + embedding similarity
    """
    return list(candidates)
