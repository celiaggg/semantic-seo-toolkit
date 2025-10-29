from __future__ import annotations

from typing import Any, Dict, List, Optional

from semantic_seo.shared.utils.logging import get_logger

_logger = get_logger(__name__)

try:
    from elasticsearch import Elasticsearch  # type: ignore
except Exception:  # pragma: no cover - optional dependency
    Elasticsearch = None  # type: ignore


class ElasticsearchClient:
    """Small helper around the official Elasticsearch Python client."""

    def __init__(self, url: str, *, username: str = "", password: str = "") -> None:
        if Elasticsearch is None:
            raise RuntimeError("elasticsearch package not installed")
        auth: Optional[tuple[str, str]] = None
        if username or password:
            auth = (username, password)
        self.es = Elasticsearch(url, basic_auth=auth)

    def upsert(self, index: str, id: str, body: Dict[str, Any]) -> Dict[str, Any]:
        return self.es.index(index=index, id=id, document=body, refresh=True)

    def bm25_search(self, index: str, query: str, *, size: int = 10) -> Dict[str, Any]:
        dsl = {
            "query": {
                "multi_match": {
                    "query": query,
                    "fields": ["title^2", "content", "entities^1.5"],
                }
            }
        }
        return self.es.search(index=index, query=dsl["query"], size=size)

    def knn_search(
        self,
        index: str,
        vector: List[float],
        *,
        field: str = "embedding",
        k: int = 10,
        num_candidates: int = 100,
        filter_query: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        body: Dict[str, Any] = {
            "knn": {
                "field": field,
                "query_vector": vector,
                "k": k,
                "num_candidates": num_candidates,
            }
        }
        if filter_query:
            body["knn"]["filter"] = filter_query
        return self.es.search(index=index, body=body)
