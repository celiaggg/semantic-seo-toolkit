from __future__ import annotations

from collections import defaultdict
from typing import Dict, Iterable, List


def build_entity_map(entities: Iterable[Dict[str, str]]) -> Dict[str, Dict[str, int]]:
    """Aggregate extracted entities into a frequency map by label.

    Returns
    -------
    Dict[label, Dict[entity_text, count]]
    """
    label_to_counts: Dict[str, Dict[str, int]] = defaultdict(lambda: defaultdict(int))
    for e in entities:
        text = e.get("text") or e.get("name")
        label = e.get("label") or e.get("type")
        if not text or not label:
            continue
        label_to_counts[str(label)][str(text)] += 1
    # Convert nested defaultdicts to regular dicts
    return {label: dict(counts) for label, counts in label_to_counts.items()}
