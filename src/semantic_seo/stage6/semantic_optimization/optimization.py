from __future__ import annotations

from typing import Iterable, List, Tuple

from semantic_seo.stage5.embeddings.embedder import SentenceTransformerEmbedder
from semantic_seo.stage4.semantic_distance.distance import cosine_similarity


def semantic_strength(content: str, required_entities: Iterable[str]) -> float:
    """Estimate semantic strength by embedding similarity to an entity phrase list."""
    embedder = SentenceTransformerEmbedder()
    target = " ".join(required_entities) or ""
    if not target:
        return 0.0
    vec_content = embedder.embed_texts([content])[0]
    vec_target = embedder.embed_texts([target])[0]
    return cosine_similarity(vec_content, vec_target)
