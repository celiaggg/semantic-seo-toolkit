### Module documentation

- `semantic_seo.stage0.persona_builder` — Build personas from CSV or other sources
- `semantic_seo.stage0.prompt_engineering` — Persona-driven conversation prompts
- `semantic_seo.stage0.context_modeling` — `Persona`, `UseCase`, `DecisionContext` models
- `semantic_seo.stage0.llm_testing` — Test LLM outputs for given contexts

- `semantic_seo.stage1.entity_extraction` — spaCy and Google NLP entity extraction
- `semantic_seo.stage1.entity_mapping` — Aggregate entities into a map
- `semantic_seo.stage1.semantic_clustering` — TF‑IDF + KMeans clustering
- `semantic_seo.stage1.entity_disambiguation` — Placeholders for disambiguation strategies

- `semantic_seo.stage2.keyword_research` — BigQuery/GSC, SEMrush placeholders
- `semantic_seo.stage2.prompt_analysis` — Extract query elements from decision contexts
- `semantic_seo.stage2.query_fanout` — LLM-based query variant generation
- `semantic_seo.stage2.conversational_query_extraction` — Parse conversational prompts

- `semantic_seo.stage3.query_classifier` — Heuristic baseline; replace with ML later
- `semantic_seo.stage3.intent_detection` — Intent heuristics
- `semantic_seo.stage3.micro_intent_mapping` — Map to content formats

- `semantic_seo.stage4.entity_expansion` — Expand entities using relations
- `semantic_seo.stage4.semantic_distance` — Cosine similarity utilities
- `semantic_seo.stage4.relationship_detection` — Co-occurrence detection

- `semantic_seo.stage5.embeddings` — Sentence-Transformers and OpenAI embedders
- `semantic_seo.stage5.gap_analysis` — Gap scores based on max similarity
- `semantic_seo.stage5.hybrid_search` — Simple hybrid fusion
- `semantic_seo.stage5.coverage_mapping` — Query-to-content mapping

- `semantic_seo.stage6.content_briefs` — Content brief generation
- `semantic_seo.stage6.competitor_analysis` — Basic extraction via trafilatura
- `semantic_seo.stage6.semantic_optimization` — Semantic strength estimates
- `semantic_seo.stage6.rag_optimization` — RAG readiness checks

- `semantic_seo.stage7.content_dilution` — Find diluted pages
- `semantic_seo.stage7.topical_authority` — Naive site focus score
- `semantic_seo.stage7.semantic_relevance_scoring` — Page-to-entity relevance

Shared modules:
- `semantic_seo.shared.config` — Pydantic config models and loader
- `semantic_seo.shared.api_clients` — OpenAI, Anthropic, Google NLP, Elasticsearch
- `semantic_seo.shared.utils` — logging, I/O, text helpers
