"""
Example: Query classification

This example demonstrates how to classify user queries by entity,
intent, and micro-intent using the QueryClassifier module.
"""

from src.config import ConfigManager
from src.query_classifier import QueryClassifier


def main():
    """Main example function."""
    
    # Initialize configuration
    config = ConfigManager()
    
    # Initialize query classifier
    classifier = QueryClassifier(config)
    
    # Example queries
    queries = [
        "What is Elasticsearch?",
        "How to optimize Elasticsearch performance?",
        "Elasticsearch vs Solr comparison",
        "Elasticsearch pricing and costs",
        "How to implement real-time search with Elasticsearch?",
        "Elasticsearch security best practices",
        "Elasticsearch cluster setup tutorial",
        "Elasticsearch API documentation",
        "Troubleshooting Elasticsearch slow queries",
        "Elasticsearch for e-commerce search"
    ]
    
    print("Classifying queries...")
    print(f"Total queries: {len(queries)}\n")
    
    # Classify individual queries
    for i, query in enumerate(queries, 1):
        print(f"--- Query {i}: {query} ---")
        classification = classifier.classify_query(query)
        
        print(f"Entity: {classification.entity}")
        print(f"Intent: {classification.intent}")
        print(f"Micro Intent: {classification.micro_intent}")
        print(f"Confidence: {classification.confidence:.2f}")
        print(f"Suggested Format: {classification.suggested_content_format}")
        print(f"Target Audience: {classification.target_audience}")
        print(f"Reasoning: {classification.reasoning}")
        print()
    
    # Classify queries in batch
    print("--- Batch Classification ---")
    classifications = classifier.classify_queries_batch(queries)
    
    # Group by patterns
    patterns = classifier.classify_queries_by_pattern(queries)
    
    print("Query patterns:")
    for pattern, query_list in patterns.items():
        print(f"\nPattern: {pattern}")
        print(f"Count: {len(query_list)}")
        for q in query_list[:3]:  # Show first 3 queries
            print(f"  - {q.query}")
        if len(query_list) > 3:
            print(f"  ... and {len(query_list) - 3} more")
    
    # Analyze query trends
    print("\n--- Query Trend Analysis ---")
    trends = classifier.analyze_query_trends(queries)
    
    print(f"Total queries analyzed: {trends['total_queries']}")
    print(f"Top entities: {trends['top_entities']}")
    print(f"Top micro intents: {trends['top_micro_intents']}")
    
    # Extract entities from queries
    print("\n--- Entity Extraction from Queries ---")
    for query in queries[:3]:  # Show first 3 queries
        entities = classifier.extract_query_entities(query)
        print(f"Query: {query}")
        print(f"Entities: {entities}")
        print()
    
    # Suggest content improvements
    print("--- Content Improvement Suggestions ---")
    sample_query = "How to optimize Elasticsearch performance?"
    sample_content = "Elasticsearch is a search engine. It can be optimized by tuning various parameters."
    
    suggestions = classifier.suggest_content_improvements(sample_query, sample_content)
    
    print(f"Query: {sample_query}")
    print(f"Current content: {sample_content}")
    print(f"Suggestions: {suggestions}")


if __name__ == "__main__":
    main()