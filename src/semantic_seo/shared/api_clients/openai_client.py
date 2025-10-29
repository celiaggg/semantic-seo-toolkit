from __future__ import annotations

import os
from typing import List, Optional

from semantic_seo.shared.utils.logging import get_logger


_logger = get_logger(__name__)

try:
    # openai>=1.0.0 style
    from openai import OpenAI  # type: ignore
except Exception:  # pragma: no cover - optional dependency
    OpenAI = None  # type: ignore


class OpenAIClient:
    """Thin wrapper around the OpenAI Python SDK.

    Falls back gracefully if the SDK is not installed.
    """

    def __init__(self, api_key: Optional[str] = None, default_model: Optional[str] = None) -> None:
        self.api_key = api_key or os.getenv("OPENAI_API_KEY")
        self.default_model = default_model or os.getenv("DEFAULT_MODEL_OPENAI", "gpt-4o-mini")
        if OpenAI is None:
            _logger.warning("openai package not installed; OpenAIClient is disabled.")
            self.client = None
        else:
            self.client = OpenAI(api_key=self.api_key)

    def generate(self, prompt: str, *, system: Optional[str] = None, model: Optional[str] = None) -> str:
        if self.client is None:
            raise RuntimeError("OpenAI client unavailable; install 'openai' and set OPENAI_API_KEY")
        model_name = model or self.default_model

        # Prefer Responses API if available, otherwise fallback to chat.completions
        try:
            resp = self.client.responses.create(
                model=model_name,
                input=prompt if system is None else None,
                messages=None if system is None else [
                    {"role": "system", "content": system},
                    {"role": "user", "content": prompt},
                ],
            )
            # Concatenate text outputs
            text_chunks: List[str] = []
            for output in resp.output_text.split("\n"):
                text_chunks.append(output)
            return "\n".join(text_chunks).strip()
        except Exception:
            chat = self.client.chat.completions.create(
                model=model_name,
                messages=[
                    *( [{"role": "system", "content": system}] if system else [] ),
                    {"role": "user", "content": prompt},
                ],
                temperature=0.2,
            )
            return (chat.choices[0].message.content or "").strip()

    def embed_texts(self, texts: List[str], *, model: str = "text-embedding-3-small") -> List[List[float]]:
        if self.client is None:
            raise RuntimeError("OpenAI client unavailable; install 'openai' and set OPENAI_API_KEY")
        resp = self.client.embeddings.create(model=model, input=texts)
        return [d.embedding for d in resp.data]
