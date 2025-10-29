"""Example: Run a hybrid search (BM25 + vector).
Requires a running Elasticsearch with an index containing 'embedding' vectors."""
from semantic_seo.shared.api_clients.elasticsearch_client import ElasticsearchClient
from semantic_seo.stage5.hybrid_search.hybrid import hybrid_search

if __name__ == "__main__":
    es = ElasticsearchClient("http://localhost:9200")
    # Example only: you must compute the vector from your embedder for the query
    query = "semantic search with elasticsearch"
    vector = [0.0] * 384  # placeholder
    resp = hybrid_search(es, index="pages", query=query, vector=vector, field="embedding", size=5)
    print(resp)
