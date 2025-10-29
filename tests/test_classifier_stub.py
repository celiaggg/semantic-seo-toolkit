from semantic_seo.stage3.query_classifier.classifier import classify_query


def test_classify_query_returns_object():
    result = classify_query("Elasticsearch vs Pinecone")
    assert result.intent in {"research", "solution-seeking", "lookup", "tutorial"}
    assert isinstance(result.micro_intent, str)
