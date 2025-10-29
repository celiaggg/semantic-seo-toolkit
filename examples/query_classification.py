"""Example: Classify a query by intent and micro-intent."""
from semantic_seo.stage3.query_classifier.classifier import classify_query

if __name__ == "__main__":
    q = "Elasticsearch vs Pinecone for vector search latency"
    print(classify_query(q))
