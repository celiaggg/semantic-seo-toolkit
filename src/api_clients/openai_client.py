"""OpenAI API client for LLM interactions."""

import openai
from typing import List, Dict, Any, Optional
from ..config import ConfigManager


class OpenAIClient:
    """Client for OpenAI API interactions."""
    
    def __init__(self, config_manager: ConfigManager):
        """Initialize the OpenAI client.
        
        Args:
            config_manager: Configuration manager instance
        """
        self.config = config_manager
        self.api_key = config_manager.get_api_key("openai")
        self.client = openai.OpenAI(api_key=self.api_key)
        
        # Get model settings
        self.model = config_manager.get("apis.openai.model", "gpt-4")
        self.temperature = config_manager.get("apis.openai.temperature", 0.7)
        self.max_tokens = config_manager.get("apis.openai.max_tokens", 2000)
    
    def generate_text(
        self,
        prompt: str,
        model: Optional[str] = None,
        temperature: Optional[float] = None,
        max_tokens: Optional[int] = None,
        **kwargs
    ) -> str:
        """Generate text using OpenAI API.
        
        Args:
            prompt: Input prompt
            model: Model to use (overrides config)
            temperature: Temperature setting (overrides config)
            max_tokens: Max tokens (overrides config)
            **kwargs: Additional parameters
            
        Returns:
            Generated text
        """
        response = self.client.chat.completions.create(
            model=model or self.model,
            messages=[{"role": "user", "content": prompt}],
            temperature=temperature or self.temperature,
            max_tokens=max_tokens or self.max_tokens,
            **kwargs
        )
        
        return response.choices[0].message.content
    
    def generate_embeddings(
        self,
        texts: List[str],
        model: str = "text-embedding-ada-002"
    ) -> List[List[float]]:
        """Generate embeddings for texts.
        
        Args:
            texts: List of texts to embed
            model: Embedding model to use
            
        Returns:
            List of embedding vectors
        """
        response = self.client.embeddings.create(
            model=model,
            input=texts
        )
        
        return [data.embedding for data in response.data]
    
    def classify_text(
        self,
        text: str,
        categories: List[str],
        prompt_template: Optional[str] = None
    ) -> Dict[str, Any]:
        """Classify text into categories.
        
        Args:
            text: Text to classify
            categories: List of possible categories
            prompt_template: Custom prompt template
            
        Returns:
            Classification results
        """
        if not prompt_template:
            prompt_template = f"""
            Classify the following text into one of these categories: {', '.join(categories)}
            
            Text: {text}
            
            Return your response as JSON with the following structure:
            {{
                "category": "selected_category",
                "confidence": 0.95,
                "reasoning": "explanation"
            }}
            """
        
        response = self.generate_text(prompt_template)
        
        # Parse JSON response (simplified - in production, use proper JSON parsing)
        try:
            import json
            return json.loads(response)
        except:
            return {
                "category": categories[0],
                "confidence": 0.5,
                "reasoning": "Failed to parse response"
            }