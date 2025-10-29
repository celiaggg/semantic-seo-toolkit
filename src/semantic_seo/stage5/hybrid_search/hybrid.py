from __future__ import annotations

from typing import Any, Dict, List, Tuple

from semantic_seo.shared.api_clients.elasticsearch_client import ElasticsearchClient


def hybrid_search(
    es: ElasticsearchClient,
    index: str,
    *,
    query: str,
    vector: List[float],
    field: str = "embedding",
    size: int = 10,
) -> Dict[str, Any]:
    """Very simple hybrid by concatenating BM25 and vector scores.

    In production, consider using rank fusion, RRF, or a learning-to-rank approach.
    """
    bm25 = es.bm25_search(index=index, query=query, size=size)
    knn = es.knn_search(index=index, vector=vector, field=field, k=size)

    # Merge by doc ID with weighted sum
    scores: Dict[str, float] = {}
    def _accumulate(resp: Dict[str, Any], weight: float) -> None:
        for hit in resp.get("hits", {}).get("hits", []):
            _id = hit.get("_id")
            _score = float(hit.get("_score", 0.0))
            scores[_id] = scores.get(_id, 0.0) + weight * _score

    _accumulate(bm25, weight=0.5)
    _accumulate(knn, weight=0.5)

    # Sort and return top-N
    ranked: List[Tuple[str, float]] = sorted(scores.items(), key=lambda kv: kv[1], reverse=True)[:size]
    # Fetch sources for convenience
    out_hits: List[Dict[str, Any]] = []
    for _id, score in ranked:
        out_hits.append({"_id": _id, "_score": score})
    return {"hits": {"hits": out_hits}}
