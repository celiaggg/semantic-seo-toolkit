### Architecture overview

The project is organized as a modular pipeline aligned to the semantic SEO roadmap:

- Stage 0 — Personas & Prompt Engineering
- Stage 1 — Entity & Semantic Analysis
- Stage 2 — Keyword Research (traditional + LLM-centric)
- Stage 3 — Classification (entity, intent, micro-intent)
- Stage 4 — Entity Map Expansion
- Stage 5 — Gap Analysis (embeddings + hybrid search)
- Stage 6 — Content Recommendations and Semantic Optimization
- Stage 7 — Content Audit (dilution, topical authority, relevance)

Each stage exposes small, composable Python modules so you can adopt the whole pipeline or single components.
Shared utilities provide configuration management, logging, and API clients.

High-level data flow:
1. Build personas and decision contexts (Stage 0)
2. Extract entities and map relationships (Stage 1)
3. Collect queries (traditional + LLM prompts), expand variants (Stage 2)
4. Classify queries by entity/intent/micro-intent (Stage 3)
5. Expand the entity map and compute semantic distances (Stage 4)
6. Run gap analysis and hybrid relevance scoring against current content (Stage 5)
7. Generate content briefs and optimize/re-audit (Stages 6–7)
