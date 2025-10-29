from __future__ import annotations

from typing import Dict, Iterable, List, Tuple

from semantic_seo.stage5.embeddings.embedder import SentenceTransformerEmbedder
from semantic_seo.stage4.semantic_distance.distance import cosine_similarity


def gap_scores(
    queries: Iterable[str],
    contents: Iterable[str],
    *,
    model_name: str = "sentence-transformers/all-MiniLM-L6-v2",
) -> List[Tuple[str, float]]:
    """Compute max similarity for each query against a set of contents.

    Returns a list of (query, max_similarity) pairs. Lower scores suggest gaps.
    """
    embedder = SentenceTransformerEmbedder(model_name=model_name)
    q_list = list(queries)
    c_list = list(contents)
    q_emb = embedder.embed_texts(q_list)
    c_emb = embedder.embed_texts(c_list)
    scores: List[Tuple[str, float]] = []
    for i, q in enumerate(q_list):
        sims = [cosine_similarity(q_emb[i], c_vec) for c_vec in c_emb]
        scores.append((q, max(sims) if sims else 0.0))
    return scores
