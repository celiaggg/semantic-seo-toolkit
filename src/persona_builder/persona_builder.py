"""Persona builder for creating user personas from customer data."""

import pandas as pd
from typing import List, Dict, Any, Optional
from dataclasses import dataclass
from ..config import ConfigManager
from ..api_clients import OpenAIClient


@dataclass
class Persona:
    """Represents a user persona."""
    
    name: str
    role: str
    company_size: str
    industry: str
    pain_points: List[str]
    goals: List[str]
    use_cases: List[str]
    decision_context: str
    technical_level: str
    budget_range: str
    timeline: str
    preferred_content_formats: List[str]
    search_behavior: Dict[str, Any]
    llm_prompts: List[str]


class PersonaBuilder:
    """Builds user personas from customer data and feedback."""
    
    def __init__(self, config_manager: ConfigManager):
        """Initialize the persona builder.
        
        Args:
            config_manager: Configuration manager instance
        """
        self.config = config_manager
        self.openai_client = OpenAIClient(config_manager)
    
    def build_from_data(
        self,
        customer_data_path: str,
        sales_feedback_path: Optional[str] = None,
        community_data_path: Optional[str] = None
    ) -> List[Persona]:
        """Build personas from customer data files.
        
        Args:
            customer_data_path: Path to customer data CSV
            sales_feedback_path: Path to sales feedback CSV
            community_data_path: Path to community discussion data
            
        Returns:
            List of constructed personas
        """
        # Load customer data
        customer_df = pd.read_csv(customer_data_path)
        
        # Load additional data if available
        sales_df = None
        community_df = None
        
        if sales_feedback_path:
            sales_df = pd.read_csv(sales_feedback_path)
        
        if community_data_path:
            community_df = pd.read_csv(community_data_path)
        
        # Analyze data to identify persona patterns
        persona_patterns = self._analyze_persona_patterns(customer_df, sales_df, community_df)
        
        # Generate personas using LLM
        personas = []
        for pattern in persona_patterns:
            persona = self._generate_persona_from_pattern(pattern)
            personas.append(persona)
        
        return personas
    
    def _analyze_persona_patterns(
        self,
        customer_df: pd.DataFrame,
        sales_df: Optional[pd.DataFrame],
        community_df: Optional[pd.DataFrame]
    ) -> List[Dict[str, Any]]:
        """Analyze data to identify persona patterns.
        
        Args:
            customer_df: Customer data
            sales_df: Sales feedback data
            community_df: Community discussion data
            
        Returns:
            List of persona patterns
        """
        patterns = []
        
        # Analyze customer data
        if 'company_size' in customer_df.columns and 'industry' in customer_df.columns:
            size_industry_groups = customer_df.groupby(['company_size', 'industry']).size().reset_index(name='count')
            
            for _, row in size_industry_groups.iterrows():
                if row['count'] >= 5:  # Minimum threshold for pattern
                    patterns.append({
                        'company_size': row['company_size'],
                        'industry': row['industry'],
                        'frequency': row['count'],
                        'source': 'customer_data'
                    })
        
        # Analyze sales feedback for pain points and goals
        if sales_df is not None and 'pain_points' in sales_df.columns:
            pain_point_patterns = sales_df['pain_points'].value_counts().head(10)
            for pain_point, count in pain_point_patterns.items():
                patterns.append({
                    'pain_point': pain_point,
                    'frequency': count,
                    'source': 'sales_feedback'
                })
        
        return patterns
    
    def _generate_persona_from_pattern(self, pattern: Dict[str, Any]) -> Persona:
        """Generate a persona from a pattern using LLM.
        
        Args:
            pattern: Persona pattern data
            
        Returns:
            Generated persona
        """
        prompt = f"""
        Based on the following customer data pattern, create a detailed user persona:
        
        Pattern: {pattern}
        
        Create a persona with the following structure:
        - Name: A realistic name
        - Role: Their job title/role
        - Company Size: {pattern.get('company_size', 'Unknown')}
        - Industry: {pattern.get('industry', 'Unknown')}
        - Pain Points: 3-5 specific pain points
        - Goals: 3-5 specific goals
        - Use Cases: 3-5 specific use cases
        - Decision Context: How they make decisions
        - Technical Level: Beginner/Intermediate/Advanced
        - Budget Range: Low/Medium/High
        - Timeline: Urgency level
        - Preferred Content Formats: List of formats they prefer
        - Search Behavior: How they search for information
        - LLM Prompts: 3-5 example prompts they might use with LLMs
        
        Return the response as a structured JSON object.
        """
        
        response = self.openai_client.generate_text(prompt)
        
        # Parse response and create Persona object
        try:
            import json
            persona_data = json.loads(response)
            
            return Persona(
                name=persona_data.get('name', 'Unknown'),
                role=persona_data.get('role', 'Unknown'),
                company_size=persona_data.get('company_size', 'Unknown'),
                industry=persona_data.get('industry', 'Unknown'),
                pain_points=persona_data.get('pain_points', []),
                goals=persona_data.get('goals', []),
                use_cases=persona_data.get('use_cases', []),
                decision_context=persona_data.get('decision_context', ''),
                technical_level=persona_data.get('technical_level', 'Intermediate'),
                budget_range=persona_data.get('budget_range', 'Medium'),
                timeline=persona_data.get('timeline', 'Medium'),
                preferred_content_formats=persona_data.get('preferred_content_formats', []),
                search_behavior=persona_data.get('search_behavior', {}),
                llm_prompts=persona_data.get('llm_prompts', [])
            )
        except Exception as e:
            print(f"Error parsing persona data: {e}")
            # Return a default persona
            return Persona(
                name="Default Persona",
                role="Unknown",
                company_size=pattern.get('company_size', 'Unknown'),
                industry=pattern.get('industry', 'Unknown'),
                pain_points=[],
                goals=[],
                use_cases=[],
                decision_context="",
                technical_level="Intermediate",
                budget_range="Medium",
                timeline="Medium",
                preferred_content_formats=[],
                search_behavior={},
                llm_prompts=[]
            )
    
    def build_from_community_discussions(
        self,
        discussions: List[Dict[str, Any]],
        min_engagement: int = 5
    ) -> List[Persona]:
        """Build personas from community discussions.
        
        Args:
            discussions: List of discussion data
            min_engagement: Minimum engagement threshold
            
        Returns:
            List of personas
        """
        # Filter discussions by engagement
        high_engagement = [
            d for d in discussions 
            if d.get('engagement_score', 0) >= min_engagement
        ]
        
        # Group by common themes
        themes = self._extract_themes(high_engagement)
        
        personas = []
        for theme in themes:
            persona = self._generate_persona_from_theme(theme)
            personas.append(persona)
        
        return personas
    
    def _extract_themes(self, discussions: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """Extract common themes from discussions.
        
        Args:
            discussions: List of discussion data
            
        Returns:
            List of themes
        """
        # Simple theme extraction based on common keywords
        # In production, this would use more sophisticated NLP
        themes = {}
        
        for discussion in discussions:
            content = discussion.get('content', '').lower()
            
            # Define theme keywords
            theme_keywords = {
                'performance': ['slow', 'performance', 'speed', 'optimization'],
                'scalability': ['scale', 'scaling', 'large', 'volume'],
                'integration': ['integrate', 'api', 'connect', 'setup'],
                'cost': ['cost', 'price', 'expensive', 'budget'],
                'security': ['security', 'secure', 'compliance', 'privacy']
            }
            
            for theme, keywords in theme_keywords.items():
                if any(keyword in content for keyword in keywords):
                    if theme not in themes:
                        themes[theme] = []
                    themes[theme].append(discussion)
        
        return [
            {'theme': theme, 'discussions': discussions}
            for theme, discussions in themes.items()
        ]
    
    def _generate_persona_from_theme(self, theme_data: Dict[str, Any]) -> Persona:
        """Generate persona from theme data.
        
        Args:
            theme_data: Theme and discussion data
            
        Returns:
            Generated persona
        """
        theme = theme_data['theme']
        discussions = theme_data['discussions']
        
        prompt = f"""
        Based on community discussions about {theme}, create a user persona:
        
        Theme: {theme}
        Sample discussions: {discussions[:3]}  # First 3 discussions
        
        Create a persona that represents users who discuss {theme} issues.
        Include their pain points, goals, and how they would interact with LLMs.
        """
        
        response = self.openai_client.generate_text(prompt)
        
        # Parse and create persona (similar to _generate_persona_from_pattern)
        # Implementation would be similar to the pattern-based generation
        return Persona(
            name=f"{theme.title()} User",
            role="Community Member",
            company_size="Unknown",
            industry="Unknown",
            pain_points=[theme],
            goals=[],
            use_cases=[],
            decision_context="",
            technical_level="Intermediate",
            budget_range="Unknown",
            timeline="Unknown",
            preferred_content_formats=[],
            search_behavior={},
            llm_prompts=[]
        )