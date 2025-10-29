from __future__ import annotations

from typing import Iterable, List, Optional

from semantic_seo.shared.utils.logging import get_logger

_logger = get_logger(__name__)

try:
    from sentence_transformers import SentenceTransformer  # type: ignore
except Exception:  # pragma: no cover - optional dependency
    SentenceTransformer = None  # type: ignore


class SentenceTransformerEmbedder:
    """Embed texts using a local Sentence-Transformers model."""

    def __init__(self, model_name: str = "sentence-transformers/all-MiniLM-L6-v2") -> None:
        if SentenceTransformer is None:
            raise RuntimeError(
                "sentence-transformers is not installed. Add it to requirements and install."
            )
        self.model = SentenceTransformer(model_name)

    def embed_texts(self, texts: Iterable[str], *, batch_size: int = 64) -> List[List[float]]:
        return [list(vec) for vec in self.model.encode(list(texts), batch_size=batch_size, show_progress_bar=False)]


class OpenAIEmbedder:
    """Embed texts using OpenAI embeddings API."""

    def __init__(self, model: str = "text-embedding-3-small") -> None:
        from semantic_seo.shared.api_clients.openai_client import OpenAIClient

        self.model = model
        self.client = OpenAIClient()

    def embed_texts(self, texts: Iterable[str]) -> List[List[float]]:
        return self.client.embed_texts(list(texts), model=self.model)
