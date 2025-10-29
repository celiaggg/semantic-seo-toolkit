"""Example: Extract entities using spaCy."""
from semantic_seo.stage1.entity_extraction.spacy_extractor import SpacyEntityExtractor

if __name__ == "__main__":
    text = "Elasticsearch is a vector database used for semantic search and RAG."
    extractor = SpacyEntityExtractor()
    ents = extractor.extract(text)
    print(ents)
