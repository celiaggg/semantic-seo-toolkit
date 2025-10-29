"""Application settings and configuration models."""

from typing import List, Optional, Dict, Any
from pydantic import BaseModel, Field


class APISettings(BaseModel):
    """API configuration settings."""
    
    openai_model: str = Field(default="gpt-4", description="OpenAI model to use")
    openai_temperature: float = Field(default=0.7, ge=0.0, le=2.0)
    openai_max_tokens: int = Field(default=2000, gt=0)
    
    anthropic_model: str = Field(default="claude-3-sonnet-20240229")
    anthropic_max_tokens: int = Field(default=2000, gt=0)
    
    google_nlp_model: str = Field(default="text-bison@001")
    google_nlp_confidence_threshold: float = Field(default=0.7, ge=0.0, le=1.0)


class EntityExtractionSettings(BaseModel):
    """Entity extraction configuration."""
    
    spacy_model: str = Field(default="en_core_web_lg")
    confidence_threshold: float = Field(default=0.8, ge=0.0, le=1.0)
    entity_types: List[str] = Field(default=[
        "PERSON", "ORG", "GPE", "PRODUCT", "TECHNOLOGY", "CONCEPT"
    ])


class SemanticClusteringSettings(BaseModel):
    """Semantic clustering configuration."""
    
    algorithm: str = Field(default="kmeans")
    n_clusters: int = Field(default=10, gt=0)
    min_cluster_size: int = Field(default=5, gt=0)
    similarity_threshold: float = Field(default=0.7, ge=0.0, le=1.0)


class QueryClassificationSettings(BaseModel):
    """Query classification configuration."""
    
    micro_intents: List[str] = Field(default=[
        "documentation", "tutorial", "comparison", "troubleshooting", 
        "solution", "reference"
    ])
    entity_types: List[str] = Field(default=[
        "product", "technology", "concept", "use_case"
    ])


class GapAnalysisSettings(BaseModel):
    """Gap analysis configuration."""
    
    similarity_threshold: float = Field(default=0.6, ge=0.0, le=1.0)
    min_content_length: int = Field(default=500, gt=0)
    max_gap_score: float = Field(default=0.3, ge=0.0, le=1.0)


class ContentOptimizationSettings(BaseModel):
    """Content optimization configuration."""
    
    min_semantic_score: float = Field(default=0.7, ge=0.0, le=1.0)
    target_word_count: int = Field(default=2000, gt=0)
    max_heading_depth: int = Field(default=3, gt=0)


class DataSourceSettings(BaseModel):
    """Data source configuration."""
    
    bigquery_project_id: Optional[str] = None
    bigquery_dataset: str = Field(default="semantic_seo")
    
    elasticsearch_hosts: List[str] = Field(default=["localhost:9200"])
    elasticsearch_index_prefix: str = Field(default="semantic_seo")
    
    gsc_site_url: Optional[str] = None
    gsc_start_date: str = Field(default="2023-01-01")
    gsc_end_date: str = Field(default="2024-01-01")


class MonitoringSettings(BaseModel):
    """Monitoring and logging configuration."""
    
    enable_metrics: bool = Field(default=True)
    metrics_port: int = Field(default=8000, gt=0)
    log_retention_days: int = Field(default=30, gt=0)


class Settings(BaseModel):
    """Main application settings."""
    
    app_name: str = Field(default="Semantic SEO Strategy")
    app_version: str = Field(default="0.1.0")
    debug: bool = Field(default=True)
    log_level: str = Field(default="INFO")
    
    apis: APISettings = Field(default_factory=APISettings)
    entity_extraction: EntityExtractionSettings = Field(default_factory=EntityExtractionSettings)
    semantic_clustering: SemanticClusteringSettings = Field(default_factory=SemanticClusteringSettings)
    query_classification: QueryClassificationSettings = Field(default_factory=QueryClassificationSettings)
    gap_analysis: GapAnalysisSettings = Field(default_factory=GapAnalysisSettings)
    content_optimization: ContentOptimizationSettings = Field(default_factory=ContentOptimizationSettings)
    data_sources: DataSourceSettings = Field(default_factory=DataSourceSettings)
    monitoring: MonitoringSettings = Field(default_factory=MonitoringSettings)