from __future__ import annotations

from pydantic import BaseModel, Field
from typing import Optional, Dict


class OpenAIConfig(BaseModel):
    model: str = Field(default="gpt-4o-mini")


class AnthropicConfig(BaseModel):
    model: str = Field(default="claude-3-5-sonnet")


class LLMConfig(BaseModel):
    openai: OpenAIConfig = Field(default_factory=OpenAIConfig)
    anthropic: AnthropicConfig = Field(default_factory=AnthropicConfig)


class EmbeddingsConfig(BaseModel):
    provider: str = Field(default="sentence-transformers")  # or "openai"
    model_name: str = Field(default="sentence-transformers/all-MiniLM-L6-v2")
    batch_size: int = Field(default=64)


class NLPConfig(BaseModel):
    spacy_model: str = Field(default="en_core_web_md")


class ElasticsearchIndices(BaseModel):
    pages: str = Field(default="pages")
    chunks: str = Field(default="chunks")
    queries: str = Field(default="queries")


class ElasticsearchConfig(BaseModel):
    url: str = Field(default="http://localhost:9200")
    username: str = Field(default="")
    password: str = Field(default="")
    indices: ElasticsearchIndices = Field(default_factory=ElasticsearchIndices)


class BigQueryConfig(BaseModel):
    project_id: Optional[str] = None
    dataset: Optional[str] = None


class DataSourcesConfig(BaseModel):
    gsc: Dict[str, str] = Field(default_factory=dict)
    bigquery: BigQueryConfig = Field(default_factory=BigQueryConfig)
    semrush: Dict[str, str] = Field(default_factory=dict)


class PipelineStageFlags(BaseModel):
    personas_enabled: bool = True
    prompt_generation_enabled: bool = True
    entity_extraction_enabled: bool = True
    keyword_research_enabled: bool = True
    classification_enabled: bool = True
    entity_expansion_enabled: bool = True
    gap_analysis_enabled: bool = True
    content_recommendations_enabled: bool = True
    content_audit_enabled: bool = True


class PipelineConfig(BaseModel):
    stage0: PipelineStageFlags = Field(default_factory=PipelineStageFlags)
    stage1: PipelineStageFlags = Field(default_factory=PipelineStageFlags)
    stage2: PipelineStageFlags = Field(default_factory=PipelineStageFlags)
    stage3: PipelineStageFlags = Field(default_factory=PipelineStageFlags)
    stage4: PipelineStageFlags = Field(default_factory=PipelineStageFlags)
    stage5: PipelineStageFlags = Field(default_factory=PipelineStageFlags)
    stage6: PipelineStageFlags = Field(default_factory=PipelineStageFlags)
    stage7: PipelineStageFlags = Field(default_factory=PipelineStageFlags)


class ProjectConfig(BaseModel):
    name: str = Field(default="semantic-seo")
    environment: str = Field(default="dev")


class AppConfig(BaseModel):
    project: ProjectConfig = Field(default_factory=ProjectConfig)
    nlp: NLPConfig = Field(default_factory=NLPConfig)
    embeddings: EmbeddingsConfig = Field(default_factory=EmbeddingsConfig)
    llm: LLMConfig = Field(default_factory=LLMConfig)
    elasticsearch: ElasticsearchConfig = Field(default_factory=ElasticsearchConfig)
    data_sources: DataSourcesConfig = Field(default_factory=DataSourcesConfig)
    pipeline: PipelineConfig = Field(default_factory=PipelineConfig)
