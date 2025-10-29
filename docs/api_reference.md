### API reference

This project provides a lightweight API surface. Key entry points:

- Config
  - `semantic_seo.shared.config.loader.load_config(path=None)` -> `AppConfig`

- Stage 0
  - `semantic_seo.stage0.persona_builder.builder.build_personas_from_csv(path)`
  - `semantic_seo.stage0.prompt_engineering.generator.generate_conversation_prompts(context)`
  - `semantic_seo.stage0.llm_testing.evaluator.LLMTester.run(context)`

- Stage 1
  - `semantic_seo.stage1.entity_extraction.spacy_extractor.SpacyEntityExtractor.extract(text)`
  - `semantic_seo.stage1.entity_extraction.gcloud_extractor.GoogleEntityExtractor.extract(text)`
  - `semantic_seo.stage1.entity_mapping.map_builder.build_entity_map(entities)`

- Stage 2
  - `semantic_seo.stage2.keyword_research.gsc_bigquery.fetch_gsc_queries(table_fqn)`
  - `semantic_seo.stage2.query_fanout.expand.query_fanout(seed_query)`
  - `semantic_seo.stage2.conversational_query_extraction.extractor.extract_from_prompt(prompt)`

- Stage 3
  - `semantic_seo.stage3.query_classifier.classifier.classify_query(query)`

- Stage 4
  - `semantic_seo.stage4.semantic_distance.distance.cosine_similarity(a, b)`

- Stage 5
  - `semantic_seo.stage5.embeddings.embedder.SentenceTransformerEmbedder`
  - `semantic_seo.stage5.gap_analysis.gaps.gap_scores(queries, contents)`
  - `semantic_seo.stage5.hybrid_search.hybrid.hybrid_search(es, index, query, vector)`

- Stage 6
  - `semantic_seo.stage6.content_briefs.briefs.generate_brief(topic, micro_intent, entities)`

- Stage 7
  - `semantic_seo.stage7.semantic_relevance_scoring.scoring.page_relevance_scores(pages, entity_phrase)`
