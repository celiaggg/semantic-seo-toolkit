### Setup guides

1) Environment and installation
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pip install -e .
cp .env.example .env
cp config.yaml.example config.yaml
```

2) Google Cloud
- Set `GOOGLE_APPLICATION_CREDENTIALS` in `.env`
- Enable the Natural Language, BigQuery, and Storage APIs as needed

3) Elasticsearch
- Set `ELASTICSEARCH_URL`, `ELASTICSEARCH_USERNAME`, `ELASTICSEARCH_PASSWORD`
- Create indices as per `config.yaml.example`

4) LLM APIs
- Set `OPENAI_API_KEY` or `ANTHROPIC_API_KEY`

5) spaCy model
```bash
python -m spacy download en_core_web_md
```
