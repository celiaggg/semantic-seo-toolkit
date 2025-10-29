# Semantic SEO Toolkit

A modular Python project implementing a full semantic SEO strategy: persona research → prompt engineering → entity extraction and mapping → query classification → gap analysis → content recommendations and semantic optimization. The toolkit is designed to be used end-to-end or as independent components.

## Goals and vision
- Build an entity-driven, machine-understandable knowledge architecture.
- Align content with real user contexts, intents, and micro-intents.
- Modernize keyword research with LLM-centric prompt analysis and query fan-out.
- Automate semantic clustering, gap analysis, and hybrid relevance scoring (BM25 + vectors).
- Optimize content for both search engines and LLM/RAG retrieval.

This project is informed by the roadmap in `ROADMAP.md` and organizes modules by stages from Stage 0 (Personas & Prompts) through Stage 7 (Content Audit).

## Installation

### Prerequisites
- Python 3.10+
- Access keys for any APIs you plan to use (OpenAI, Anthropic, Google Cloud, Elasticsearch)

### Steps
```bash
# 1) Create and activate a virtual environment
python -m venv .venv
source .venv/bin/activate

# 2) Install dependencies
pip install -r requirements.txt

# 3) Install the package in editable mode
pip install -e .

# 4) Configure environment and project settings
cp .env.example .env
cp config.yaml.example config.yaml
```

## Quick start

```python
from semantic_seo.shared.config.loader import load_config
from semantic_seo.stage5.embeddings.embedder import SentenceTransformerEmbedder

config = load_config("config.yaml")
embedder = SentenceTransformerEmbedder(model_name=config.embeddings.model_name)
embeddings = embedder.embed_texts(["Elasticsearch is a vector database for semantic search."])
print(len(embeddings), len(embeddings[0]))
```

- See `examples/` for runnable scripts:
  - `personas_from_customer_data.py`
  - `generate_and_test_prompts.py`
  - `entity_extraction_spacy.py`
  - `query_classification.py`
  - `gap_analysis_example.py`
  - `hybrid_search_example.py`

## Project layout
- `src/semantic_seo/` — modules organized by roadmap stages
  - `stage0/` Personas & Prompt Engineering
  - `stage1/` Entity & Semantic Analysis
  - `stage2/` Keyword Research
  - `stage3/` Classification
  - `stage4/` Entity Map Expansion
  - `stage5/` Gap Analysis
  - `stage6/` Content Recommendations
  - `stage7/` Content Audit
- `src/semantic_seo/shared/` — `utils/`, `config/`, `api_clients/`
- `examples/` — usage examples
- `docs/` — architecture, module docs, guides, API reference
- `tests/` — unit tests

## Links to documentation
- Architecture overview: `docs/architecture.md`
- Module documentation: `docs/modules.md`
- Persona development guide: `docs/persona_development.md`
- Prompt engineering best practices: `docs/prompt_engineering.md`
- API reference: `docs/api_reference.md`
- Setup guides: `docs/setup_guides.md`

## License
MIT (add your organization’s preferred license if different).
