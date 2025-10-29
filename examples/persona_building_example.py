"""
Example: Building personas from customer data

This example demonstrates how to build user personas from customer data,
sales feedback, and community discussions using the PersonaBuilder module.
"""

import pandas as pd
from src.config import ConfigManager
from src.persona_builder import PersonaBuilder


def main():
    """Main example function."""
    
    # Initialize configuration
    config = ConfigManager()
    
    # Initialize persona builder
    persona_builder = PersonaBuilder(config)
    
    # Example customer data
    customer_data = {
        'company_size': ['Startup', 'Enterprise', 'Mid-market', 'Startup', 'Enterprise'],
        'industry': ['Technology', 'Finance', 'Healthcare', 'E-commerce', 'Technology'],
        'role': ['CTO', 'Data Engineer', 'DevOps Engineer', 'Product Manager', 'Solutions Architect'],
        'pain_points': [
            'Search performance at scale',
            'Data integration complexity',
            'Security compliance',
            'Cost optimization',
            'Real-time analytics'
        ]
    }
    
    # Create DataFrame
    customer_df = pd.DataFrame(customer_data)
    customer_df.to_csv('customer_data.csv', index=False)
    
    # Example sales feedback data
    sales_feedback = {
        'pain_points': [
            'Search performance at scale',
            'Data integration complexity',
            'Security compliance',
            'Cost optimization',
            'Real-time analytics',
            'Search performance at scale',
            'Data integration complexity'
        ],
        'goals': [
            'Improve search speed',
            'Simplify data pipeline',
            'Meet compliance requirements',
            'Reduce infrastructure costs',
            'Enable real-time insights',
            'Scale search infrastructure',
            'Streamline data workflows'
        ]
    }
    
    sales_df = pd.DataFrame(sales_feedback)
    sales_df.to_csv('sales_feedback.csv', index=False)
    
    # Example community discussions
    community_data = {
        'content': [
            'How to optimize Elasticsearch for large datasets?',
            'Best practices for security in Elasticsearch?',
            'Cost-effective scaling strategies?',
            'Real-time analytics with Elasticsearch?',
            'Integration with existing data pipelines?'
        ],
        'engagement_score': [8, 7, 6, 9, 5]
    }
    
    community_df = pd.DataFrame(community_data)
    community_df.to_csv('community_data.csv', index=False)
    
    # Build personas from data
    print("Building personas from customer data...")
    personas = persona_builder.build_from_data(
        customer_data_path='customer_data.csv',
        sales_feedback_path='sales_feedback.csv',
        community_data_path='community_data.csv'
    )
    
    # Display results
    print(f"\nGenerated {len(personas)} personas:")
    for i, persona in enumerate(personas, 1):
        print(f"\n--- Persona {i}: {persona.name} ---")
        print(f"Role: {persona.role}")
        print(f"Company Size: {persona.company_size}")
        print(f"Industry: {persona.industry}")
        print(f"Pain Points: {persona.pain_points}")
        print(f"Goals: {persona.goals}")
        print(f"Use Cases: {persona.use_cases}")
        print(f"Technical Level: {persona.technical_level}")
        print(f"LLM Prompts: {persona.llm_prompts}")
    
    # Build personas from community discussions
    print("\n\nBuilding personas from community discussions...")
    discussions = [
        {
            'content': 'How to optimize Elasticsearch for large datasets?',
            'engagement_score': 8,
            'theme': 'performance'
        },
        {
            'content': 'Best practices for security in Elasticsearch?',
            'engagement_score': 7,
            'theme': 'security'
        }
    ]
    
    community_personas = persona_builder.build_from_community_discussions(discussions)
    
    print(f"\nGenerated {len(community_personas)} personas from community data:")
    for i, persona in enumerate(community_personas, 1):
        print(f"\n--- Community Persona {i}: {persona.name} ---")
        print(f"Pain Points: {persona.pain_points}")


if __name__ == "__main__":
    main()