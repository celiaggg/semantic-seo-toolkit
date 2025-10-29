"""Example: Compute gap scores between queries and content set."""
from semantic_seo.stage5.gap_analysis.gaps import gap_scores

if __name__ == "__main__":
    queries = [
        "elasticsearch vector database",
        "hybrid search bm25 and vectors",
        "rag pipeline with elasticsearch",
    ]
    contents = [
        "Elasticsearch supports dense_vector fields and ANN for semantic search.",
        "Combine BM25 with vector similarity for best relevance.",
    ]
    print(gap_scores(queries, contents))
