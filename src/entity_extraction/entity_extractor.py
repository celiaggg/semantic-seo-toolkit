"""Entity extractor using spaCy and Google NLP API."""

import spacy
from typing import List, Dict, Any, Optional, Tuple
from dataclasses import dataclass
from ..config import ConfigManager
from ..api_clients import GoogleNLPClient, OpenAIClient


@dataclass
class Entity:
    """Represents an extracted entity."""
    
    text: str
    label: str
    start: int
    end: int
    confidence: float
    description: Optional[str] = None
    category: Optional[str] = None
    source: str = "spacy"  # spacy, google_nlp, or hybrid


class EntityExtractor:
    """Extracts entities from text using multiple methods."""
    
    def __init__(self, config_manager: ConfigManager):
        """Initialize the entity extractor.
        
        Args:
            config_manager: Configuration manager instance
        """
        self.config = config_manager
        self.confidence_threshold = config_manager.get("entity_extraction.confidence_threshold", 0.8)
        
        # Initialize spaCy
        spacy_model = config_manager.get("entity_extraction.spacy_model", "en_core_web_lg")
        try:
            self.nlp = spacy.load(spacy_model)
        except OSError:
            print(f"Warning: {spacy_model} not found. Using en_core_web_sm.")
            self.nlp = spacy.load("en_core_web_sm")
        
        # Initialize API clients
        try:
            self.google_nlp_client = GoogleNLPClient(config_manager)
        except Exception as e:
            print(f"Warning: Google NLP client not available: {e}")
            self.google_nlp_client = None
        
        self.openai_client = OpenAIClient(config_manager)
    
    def extract_entities(
        self,
        text: str,
        methods: List[str] = None,
        entity_types: List[str] = None
    ) -> List[Entity]:
        """Extract entities from text using specified methods.
        
        Args:
            text: Input text
            methods: List of extraction methods ['spacy', 'google_nlp', 'hybrid']
            entity_types: List of entity types to extract
            
        Returns:
            List of extracted entities
        """
        if methods is None:
            methods = ['spacy']
        
        if entity_types is None:
            entity_types = self.config.get("entity_extraction.entity_types", [
                "PERSON", "ORG", "GPE", "PRODUCT", "TECHNOLOGY", "CONCEPT"
            ])
        
        entities = []
        
        # Extract using spaCy
        if 'spacy' in methods:
            spacy_entities = self._extract_with_spacy(text, entity_types)
            entities.extend(spacy_entities)
        
        # Extract using Google NLP
        if 'google_nlp' in methods and self.google_nlp_client:
            google_entities = self._extract_with_google_nlp(text, entity_types)
            entities.extend(google_entities)
        
        # Hybrid extraction
        if 'hybrid' in methods:
            hybrid_entities = self._extract_hybrid(text, entity_types)
            entities.extend(hybrid_entities)
        
        # Remove duplicates and filter by confidence
        entities = self._deduplicate_entities(entities)
        entities = [e for e in entities if e.confidence >= self.confidence_threshold]
        
        return entities
    
    def _extract_with_spacy(self, text: str, entity_types: List[str]) -> List[Entity]:
        """Extract entities using spaCy.
        
        Args:
            text: Input text
            entity_types: List of entity types to extract
            
        Returns:
            List of entities
        """
        doc = self.nlp(text)
        entities = []
        
        for ent in doc.ents:
            if ent.label_ in entity_types:
                entity = Entity(
                    text=ent.text,
                    label=ent.label_,
                    start=ent.start_char,
                    end=ent.end_char,
                    confidence=1.0,  # spaCy doesn't provide confidence by default
                    source="spacy"
                )
                entities.append(entity)
        
        return entities
    
    def _extract_with_google_nlp(self, text: str, entity_types: List[str]) -> List[Entity]:
        """Extract entities using Google NLP API.
        
        Args:
            text: Input text
            entity_types: List of entity types to extract
            
        Returns:
            List of entities
        """
        if not self.google_nlp_client:
            return []
        
        try:
            response = self.google_nlp_client.analyze_entities(text)
            entities = []
            
            for entity in response.get('entities', []):
                entity_type = entity.get('type', 'UNKNOWN')
                if entity_type in entity_types:
                    for mention in entity.get('mentions', []):
                        entity_obj = Entity(
                            text=mention.get('text', {}).get('content', ''),
                            label=entity_type,
                            start=mention.get('text', {}).get('beginOffset', 0),
                            end=mention.get('text', {}).get('beginOffset', 0) + len(mention.get('text', {}).get('content', '')),
                            confidence=entity.get('salience', 0.0),
                            description=entity.get('description', ''),
                            source="google_nlp"
                        )
                        entities.append(entity_obj)
            
            return entities
        except Exception as e:
            print(f"Error extracting entities with Google NLP: {e}")
            return []
    
    def _extract_hybrid(self, text: str, entity_types: List[str]) -> List[Entity]:
        """Extract entities using hybrid approach (LLM + pattern matching).
        
        Args:
            text: Input text
            entity_types: List of entity types to extract
            
        Returns:
            List of entities
        """
        prompt = f"""
        Extract entities from the following text and classify them into these types: {', '.join(entity_types)}
        
        Text: {text}
        
        For each entity, provide:
        - text: the actual text
        - label: the entity type
        - start: character start position
        - end: character end position
        - confidence: confidence score (0-1)
        - description: brief description
        
        Return as JSON array.
        """
        
        try:
            response = self.openai_client.generate_text(prompt)
            import json
            entities_data = json.loads(response)
            
            entities = []
            for entity_data in entities_data:
                entity = Entity(
                    text=entity_data.get('text', ''),
                    label=entity_data.get('label', 'UNKNOWN'),
                    start=entity_data.get('start', 0),
                    end=entity_data.get('end', 0),
                    confidence=entity_data.get('confidence', 0.5),
                    description=entity_data.get('description', ''),
                    source="hybrid"
                )
                entities.append(entity)
            
            return entities
        except Exception as e:
            print(f"Error in hybrid entity extraction: {e}")
            return []
    
    def _deduplicate_entities(self, entities: List[Entity]) -> List[Entity]:
        """Remove duplicate entities based on text and position.
        
        Args:
            entities: List of entities
            
        Returns:
            Deduplicated list of entities
        """
        seen = set()
        unique_entities = []
        
        for entity in entities:
            key = (entity.text.lower(), entity.start, entity.end)
            if key not in seen:
                seen.add(key)
                unique_entities.append(entity)
        
        return unique_entities
    
    def extract_entities_from_documents(
        self,
        documents: List[Dict[str, Any]],
        text_field: str = "content"
    ) -> Dict[str, List[Entity]]:
        """Extract entities from multiple documents.
        
        Args:
            documents: List of documents
            text_field: Field containing the text content
            
        Returns:
            Dictionary mapping document ID to entities
        """
        results = {}
        
        for doc in documents:
            doc_id = doc.get('id', str(hash(doc.get(text_field, ''))))
            text = doc.get(text_field, '')
            
            if text:
                entities = self.extract_entities(text)
                results[doc_id] = entities
        
        return results
    
    def extract_entity_relationships(
        self,
        text: str,
        entities: List[Entity]
    ) -> List[Dict[str, Any]]:
        """Extract relationships between entities.
        
        Args:
            text: Input text
            entities: List of entities
            
        Returns:
            List of relationships
        """
        if not self.nlp:
            return []
        
        doc = self.nlp(text)
        relationships = []
        
        # Find co-occurrences and dependencies
        for i, entity1 in enumerate(entities):
            for j, entity2 in enumerate(entities[i+1:], i+1):
                # Check if entities are in the same sentence
                sent1 = None
                sent2 = None
                
                for sent in doc.sents:
                    if entity1.start >= sent.start_char and entity1.end <= sent.end_char:
                        sent1 = sent
                    if entity2.start >= sent.start_char and entity2.end <= sent.end_char:
                        sent2 = sent
                
                if sent1 and sent2 and sent1 == sent2:
                    # Entities are in the same sentence
                    relationship = {
                        'entity1': entity1.text,
                        'entity2': entity2.text,
                        'sentence': sent1.text,
                        'type': 'co_occurrence',
                        'confidence': 0.7
                    }
                    relationships.append(relationship)
        
        return relationships