from __future__ import annotations

from typing import Iterable, List

from semantic_seo.stage5.embeddings.embedder import SentenceTransformerEmbedder
from semantic_seo.stage4.semantic_distance.distance import cosine_similarity


def page_relevance_scores(pages: Iterable[str], *, entity_phrase: str) -> List[float]:
    """Compute relevance score of each page to an entity phrase."""
    embedder = SentenceTransformerEmbedder()
    p_list = list(pages)
    if not p_list:
        return []
    page_vecs = embedder.embed_texts(p_list)
    ent_vec = embedder.embed_texts([entity_phrase])[0]
    return [cosine_similarity(vec, ent_vec) for vec in page_vecs]
