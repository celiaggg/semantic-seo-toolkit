from __future__ import annotations

from pathlib import Path
from typing import Any, Dict, Optional

import os
import yaml
from dotenv import load_dotenv

from .schema import AppConfig


def _read_yaml(path: Path) -> Dict[str, Any]:
    with path.open("r", encoding="utf-8") as f:
        return yaml.safe_load(f) or {}


def load_config(config_path: Optional[str | Path] = None, *, load_env: bool = True) -> AppConfig:
    """Load configuration from YAML file and environment variables.

    Precedence: environment variables override YAML where applicable.

    Parameters
    ----------
    config_path:
        Path to YAML config (e.g., "config.yaml"). If None, tries to find it in CWD.
    load_env:
        If True, loads environment from a local `.env` file first.
    """
    if load_env:
        load_dotenv(override=False)

    resolved: Optional[Path] = None
    if config_path is not None:
        resolved = Path(config_path)
    else:
        candidate = Path.cwd() / "config.yaml"
        if candidate.exists():
            resolved = candidate

    data: Dict[str, Any] = {}
    if resolved and resolved.exists():
        data = _read_yaml(resolved)

    # Overlay environment fallbacks
    # LLM defaults
    data.setdefault("llm", {})
    data["llm"].setdefault("openai", {})
    data["llm"]["openai"].setdefault("model", os.getenv("DEFAULT_MODEL_OPENAI", "gpt-4o-mini"))
    data["llm"].setdefault("anthropic", {})
    data["llm"]["anthropic"].setdefault("model", os.getenv("DEFAULT_MODEL_ANTHROPIC", "claude-3-5-sonnet"))

    # Embeddings
    data.setdefault("embeddings", {})
    data["embeddings"].setdefault("provider", os.getenv("EMBEDDINGS_PROVIDER", "sentence-transformers"))
    data["embeddings"].setdefault("model_name", os.getenv("SENTENCE_TRANSFORMERS_MODEL", "sentence-transformers/all-MiniLM-L6-v2"))

    # NLP
    data.setdefault("nlp", {})
    data["nlp"].setdefault("spacy_model", os.getenv("SPACY_MODEL", "en_core_web_md"))

    # Elasticsearch
    data.setdefault("elasticsearch", {})
    data["elasticsearch"].setdefault("url", os.getenv("ELASTICSEARCH_URL", "http://localhost:9200"))
    data["elasticsearch"].setdefault("username", os.getenv("ELASTICSEARCH_USERNAME", ""))
    data["elasticsearch"].setdefault("password", os.getenv("ELASTICSEARCH_PASSWORD", ""))

    return AppConfig.model_validate(data)
