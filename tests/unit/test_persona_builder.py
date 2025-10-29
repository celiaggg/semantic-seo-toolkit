"""Unit tests for PersonaBuilder module."""

import pytest
import pandas as pd
from unittest.mock import Mock, patch
from src.config import ConfigManager
from src.persona_builder import PersonaBuilder, Persona


class TestPersonaBuilder:
    """Test cases for PersonaBuilder class."""
    
    @pytest.fixture
    def config_manager(self):
        """Create a mock config manager."""
        config = Mock(spec=ConfigManager)
        config.get.return_value = "test_value"
        config.get_api_key.return_value = "test_api_key"
        return config
    
    @pytest.fixture
    def persona_builder(self, config_manager):
        """Create a PersonaBuilder instance."""
        with patch('src.persona_builder.OpenAIClient'):
            return PersonaBuilder(config_manager)
    
    def test_persona_creation(self):
        """Test creating a Persona object."""
        persona = Persona(
            name="Test Persona",
            role="Data Engineer",
            company_size="Mid-market",
            industry="Technology",
            pain_points=["Performance issues"],
            goals=["Improve search speed"],
            use_cases=["E-commerce search"],
            decision_context="Technical evaluation",
            technical_level="Advanced",
            budget_range="Medium",
            timeline="3 months",
            preferred_content_formats=["Technical docs"],
            search_behavior={"queries_per_day": 10},
            llm_prompts=["How to optimize Elasticsearch?"]
        )
        
        assert persona.name == "Test Persona"
        assert persona.role == "Data Engineer"
        assert len(persona.pain_points) == 1
        assert len(persona.llm_prompts) == 1
    
    def test_analyze_persona_patterns(self, persona_builder):
        """Test analyzing persona patterns from data."""
        # Create test data
        customer_data = pd.DataFrame({
            'company_size': ['Startup', 'Enterprise', 'Startup'],
            'industry': ['Technology', 'Finance', 'Technology'],
            'role': ['CTO', 'Data Engineer', 'Developer']
        })
        
        sales_data = pd.DataFrame({
            'pain_points': ['Performance', 'Cost', 'Performance']
        })
        
        patterns = persona_builder._analyze_persona_patterns(
            customer_data, sales_data, None
        )
        
        assert len(patterns) > 0
        assert any(p['source'] == 'customer_data' for p in patterns)
        assert any(p['source'] == 'sales_feedback' for p in patterns)
    
    def test_extract_themes(self, persona_builder):
        """Test extracting themes from discussions."""
        discussions = [
            {
                'content': 'How to optimize Elasticsearch performance?',
                'engagement_score': 8
            },
            {
                'content': 'Elasticsearch security best practices',
                'engagement_score': 7
            }
        ]
        
        themes = persona_builder._extract_themes(discussions)
        
        assert len(themes) > 0
        assert any('performance' in theme['theme'] for theme in themes)
    
    @patch('src.persona_builder.OpenAIClient')
    def test_generate_persona_from_pattern(self, mock_openai, persona_builder):
        """Test generating persona from pattern."""
        # Mock OpenAI response
        mock_response = {
            'name': 'Test Persona',
            'role': 'Data Engineer',
            'company_size': 'Mid-market',
            'industry': 'Technology',
            'pain_points': ['Performance'],
            'goals': ['Speed'],
            'use_cases': ['Search'],
            'decision_context': 'Technical',
            'technical_level': 'Advanced',
            'budget_range': 'Medium',
            'timeline': '3 months',
            'preferred_content_formats': ['Docs'],
            'search_behavior': {'queries': 10},
            'llm_prompts': ['How to optimize?']
        }
        
        mock_openai.return_value.generate_text.return_value = str(mock_response)
        
        pattern = {
            'company_size': 'Mid-market',
            'industry': 'Technology',
            'frequency': 5
        }
        
        persona = persona_builder._generate_persona_from_pattern(pattern)
        
        assert isinstance(persona, Persona)
        assert persona.company_size == 'Mid-market'
        assert persona.industry == 'Technology'
    
    def test_build_from_community_discussions(self, persona_builder):
        """Test building personas from community discussions."""
        discussions = [
            {
                'content': 'Performance optimization question',
                'engagement_score': 8,
                'theme': 'performance'
            }
        ]
        
        with patch.object(persona_builder, '_extract_themes') as mock_extract:
            with patch.object(persona_builder, '_generate_persona_from_theme') as mock_generate:
                mock_extract.return_value = [{'theme': 'performance', 'discussions': discussions}]
                mock_generate.return_value = Persona(
                    name="Performance User",
                    role="Developer",
                    company_size="Unknown",
                    industry="Unknown",
                    pain_points=["performance"],
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
                
                personas = persona_builder.build_from_community_discussions(discussions)
                
                assert len(personas) == 1
                assert personas[0].name == "Performance User"