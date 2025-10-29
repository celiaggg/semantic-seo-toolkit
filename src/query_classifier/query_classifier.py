"""Query classifier for categorizing queries by entity, intent, and micro-intent."""

from typing import List, Dict, Any, Optional, Tuple
from dataclasses import dataclass
from ..config import ConfigManager
from ..api_clients import OpenAIClient


@dataclass
class QueryClassification:
    """Represents a query classification result."""
    
    query: str
    entity: str
    intent: str
    micro_intent: str
    confidence: float
    reasoning: str
    suggested_content_format: str
    target_audience: str


class QueryClassifier:
    """Classifies queries by entity, intent, and micro-intent."""
    
    def __init__(self, config_manager: ConfigManager):
        """Initialize the query classifier.
        
        Args:
            config_manager: Configuration manager instance
        """
        self.config = config_manager
        self.openai_client = OpenAIClient(config_manager)
        
        # Get classification settings
        self.micro_intents = config_manager.get("query_classification.micro_intents", [
            "documentation", "tutorial", "comparison", "troubleshooting", 
            "solution", "reference"
        ])
        self.entity_types = config_manager.get("query_classification.entity_types", [
            "product", "technology", "concept", "use_case"
        ])
    
    def classify_query(self, query: str) -> QueryClassification:
        """Classify a single query.
        
        Args:
            query: Query to classify
            
        Returns:
            Classification result
        """
        prompt = f"""
        Classify the following query into the specified categories:
        
        Query: "{query}"
        
        Entity Types: {', '.join(self.entity_types)}
        Micro Intents: {', '.join(self.micro_intents)}
        
        Provide classification with:
        1. Entity: What is the main entity/concept being discussed?
        2. Intent: What is the user's primary intent? (informational, commercial, transactional, navigational)
        3. Micro Intent: What specific type of content are they looking for?
        4. Confidence: How confident are you in this classification? (0-1)
        5. Reasoning: Why did you choose this classification?
        6. Suggested Content Format: What format would best serve this query?
        7. Target Audience: Who is likely asking this query?
        
        Return as JSON with these fields.
        """
        
        try:
            response = self.openai_client.generate_text(prompt)
            import json
            classification_data = json.loads(response)
            
            return QueryClassification(
                query=query,
                entity=classification_data.get('entity', 'unknown'),
                intent=classification_data.get('intent', 'informational'),
                micro_intent=classification_data.get('micro_intent', 'documentation'),
                confidence=classification_data.get('confidence', 0.5),
                reasoning=classification_data.get('reasoning', ''),
                suggested_content_format=classification_data.get('suggested_content_format', 'article'),
                target_audience=classification_data.get('target_audience', 'general')
            )
        except Exception as e:
            print(f"Error classifying query: {e}")
            return QueryClassification(
                query=query,
                entity="unknown",
                intent="informational",
                micro_intent="documentation",
                confidence=0.0,
                reasoning=f"Error: {str(e)}",
                suggested_content_format="article",
                target_audience="general"
            )
    
    def classify_queries_batch(self, queries: List[str]) -> List[QueryClassification]:
        """Classify multiple queries in batch.
        
        Args:
            queries: List of queries to classify
            
        Returns:
            List of classification results
        """
        results = []
        
        for query in queries:
            classification = self.classify_query(query)
            results.append(classification)
        
        return results
    
    def classify_queries_by_pattern(self, queries: List[str]) -> Dict[str, List[QueryClassification]]:
        """Classify queries and group by patterns.
        
        Args:
            queries: List of queries to classify
            
        Returns:
            Dictionary grouping queries by classification patterns
        """
        classifications = self.classify_queries_batch(queries)
        
        # Group by entity + micro_intent
        patterns = {}
        for classification in classifications:
            pattern_key = f"{classification.entity}_{classification.micro_intent}"
            if pattern_key not in patterns:
                patterns[pattern_key] = []
            patterns[pattern_key].append(classification)
        
        return patterns
    
    def extract_query_entities(self, query: str) -> List[str]:
        """Extract entities mentioned in a query.
        
        Args:
            query: Query to analyze
            
        Returns:
            List of entities found in the query
        """
        prompt = f"""
        Extract all entities (products, technologies, concepts, companies, etc.) from this query:
        
        Query: "{query}"
        
        Return as a JSON array of entity strings.
        """
        
        try:
            response = self.openai_client.generate_text(prompt)
            import json
            entities = json.loads(response)
            return entities if isinstance(entities, list) else []
        except Exception as e:
            print(f"Error extracting entities from query: {e}")
            return []
    
    def suggest_content_improvements(
        self,
        query: str,
        current_content: str
    ) -> Dict[str, Any]:
        """Suggest improvements to content based on query classification.
        
        Args:
            query: Original query
            current_content: Current content to improve
            
        Returns:
            Dictionary with improvement suggestions
        """
        classification = self.classify_query(query)
        
        prompt = f"""
        Based on this query classification and current content, suggest improvements:
        
        Query: "{query}"
        Classification: {classification.micro_intent} intent for {classification.entity}
        Current Content: {current_content[:500]}...
        
        Suggest:
        1. Missing entities that should be mentioned
        2. Content structure improvements
        3. Tone and style adjustments
        4. Additional sections to add
        5. Keywords to include
        
        Return as JSON with these fields.
        """
        
        try:
            response = self.openai_client.generate_text(prompt)
            import json
            suggestions = json.loads(response)
            return suggestions
        except Exception as e:
            print(f"Error generating content suggestions: {e}")
            return {
                "missing_entities": [],
                "structure_improvements": [],
                "tone_adjustments": [],
                "additional_sections": [],
                "keywords": []
            }
    
    def analyze_query_trends(
        self,
        queries: List[str],
        time_period: Optional[str] = None
    ) -> Dict[str, Any]:
        """Analyze trends in query patterns.
        
        Args:
            queries: List of queries to analyze
            time_period: Optional time period for context
            
        Returns:
            Dictionary with trend analysis
        """
        classifications = self.classify_queries_batch(queries)
        
        # Count by entity and micro_intent
        entity_counts = {}
        micro_intent_counts = {}
        intent_counts = {}
        
        for classification in classifications:
            entity_counts[classification.entity] = entity_counts.get(classification.entity, 0) + 1
            micro_intent_counts[classification.micro_intent] = micro_intent_counts.get(classification.micro_intent, 0) + 1
            intent_counts[classification.intent] = intent_counts.get(classification.intent, 0) + 1
        
        return {
            "total_queries": len(queries),
            "entity_distribution": entity_counts,
            "micro_intent_distribution": micro_intent_counts,
            "intent_distribution": intent_counts,
            "top_entities": sorted(entity_counts.items(), key=lambda x: x[1], reverse=True)[:10],
            "top_micro_intents": sorted(micro_intent_counts.items(), key=lambda x: x[1], reverse=True)[:10],
            "time_period": time_period
        }