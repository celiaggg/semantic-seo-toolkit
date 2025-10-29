"""
Example: Entity extraction from content

This example demonstrates how to extract entities from content using
the EntityExtractor module with multiple extraction methods.
"""

from src.config import ConfigManager
from src.entity_extraction import EntityExtractor


def main():
    """Main example function."""
    
    # Initialize configuration
    config = ConfigManager()
    
    # Initialize entity extractor
    extractor = EntityExtractor(config)
    
    # Example content about Elasticsearch
    content = """
    Elasticsearch is a distributed, RESTful search and analytics engine 
    capable of solving a growing number of use cases. As the heart of the 
    Elastic Stack, it centrally stores your data so you can discover the 
    expected and uncover the unexpected.
    
    Elasticsearch is built on Apache Lucene and was first released in 2010 
    by Elastic. It provides a distributed, multitenant-capable full-text 
    search engine with an HTTP web interface and schema-free JSON documents.
    
    Key features include:
    - Real-time search and analytics
    - Distributed and scalable
    - RESTful API
    - Schema-free JSON documents
    - Multi-tenancy
    - Full-text search
    - Analytics and aggregations
    - Machine learning capabilities
    """
    
    print("Extracting entities from content...")
    print(f"Content: {content[:100]}...\n")
    
    # Extract entities using spaCy
    print("--- spaCy Extraction ---")
    spacy_entities = extractor.extract_entities(
        content, 
        methods=['spacy'],
        entity_types=['ORG', 'PRODUCT', 'TECHNOLOGY', 'CONCEPT']
    )
    
    for entity in spacy_entities:
        print(f"Entity: {entity.text}")
        print(f"Label: {entity.label}")
        print(f"Confidence: {entity.confidence}")
        print(f"Position: {entity.start}-{entity.end}")
        print(f"Source: {entity.source}")
        print()
    
    # Extract entities using hybrid method
    print("--- Hybrid Extraction ---")
    hybrid_entities = extractor.extract_entities(
        content,
        methods=['hybrid'],
        entity_types=['PRODUCT', 'TECHNOLOGY', 'CONCEPT']
    )
    
    for entity in hybrid_entities:
        print(f"Entity: {entity.text}")
        print(f"Label: {entity.label}")
        print(f"Confidence: {entity.confidence}")
        print(f"Description: {entity.description}")
        print(f"Source: {entity.source}")
        print()
    
    # Extract entity relationships
    print("--- Entity Relationships ---")
    all_entities = spacy_entities + hybrid_entities
    relationships = extractor.extract_entity_relationships(content, all_entities)
    
    for relationship in relationships:
        print(f"Entity 1: {relationship['entity1']}")
        print(f"Entity 2: {relationship['entity2']}")
        print(f"Relationship Type: {relationship['type']}")
        print(f"Sentence: {relationship['sentence']}")
        print(f"Confidence: {relationship['confidence']}")
        print()
    
    # Extract from multiple documents
    print("--- Multi-Document Extraction ---")
    documents = [
        {
            'id': 'doc1',
            'content': 'Elasticsearch is a search engine built on Lucene.',
            'title': 'Introduction to Elasticsearch'
        },
        {
            'id': 'doc2', 
            'content': 'Kibana provides visualization for Elasticsearch data.',
            'title': 'Kibana Overview'
        }
    ]
    
    doc_entities = extractor.extract_entities_from_documents(documents)
    
    for doc_id, entities in doc_entities.items():
        print(f"Document {doc_id}:")
        for entity in entities:
            print(f"  - {entity.text} ({entity.label})")
        print()


if __name__ == "__main__":
    main()