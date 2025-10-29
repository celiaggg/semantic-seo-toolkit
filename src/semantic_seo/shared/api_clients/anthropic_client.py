from __future__ import annotations

import os
from typing import Optional

from semantic_seo.shared.utils.logging import get_logger

_logger = get_logger(__name__)

try:
    import anthropic  # type: ignore
except Exception:  # pragma: no cover
    anthropic = None  # type: ignore


class AnthropicClient:
    """Thin wrapper around the Anthropics SDK for message generation."""

    def __init__(self, api_key: Optional[str] = None, default_model: Optional[str] = None) -> None:
        self.api_key = api_key or os.getenv("ANTHROPIC_API_KEY")
        self.default_model = default_model or os.getenv("DEFAULT_MODEL_ANTHROPIC", "claude-3-5-sonnet")
        if anthropic is None:
            _logger.warning("anthropic package not installed; AnthropicClient is disabled.")
            self.client = None
        else:
            self.client = anthropic.Anthropic(api_key=self.api_key)

    def generate(self, prompt: str, *, system: Optional[str] = None, model: Optional[str] = None) -> str:
        if self.client is None:
            raise RuntimeError("Anthropic client unavailable; install 'anthropic' and set ANTHROPIC_API_KEY")
        model_name = model or self.default_model
        messages = []
        if system:
            messages.append({"role": "system", "content": system})
        messages.append({"role": "user", "content": prompt})
        resp = self.client.messages.create(model=model_name, messages=messages, max_tokens=2000)
        # Concatenate any returned text blocks
        text_out = []
        for block in resp.content:
            if getattr(block, "type", None) == "text":
                text_out.append(getattr(block, "text", ""))
        return "\n".join(text_out).strip()
