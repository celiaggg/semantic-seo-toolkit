from __future__ import annotations

from dataclasses import dataclass
from typing import Literal, Optional

from semantic_seo.stage0.context_modeling.contexts import DecisionContext
from semantic_seo.stage0.prompt_engineering.generator import generate_conversation_prompts


@dataclass
class LLMTestResult:
    provider: Literal["openai", "anthropic"]
    model: str
    output: str


class LLMTester:
    def __init__(self, provider: Literal["openai", "anthropic"], model: Optional[str] = None) -> None:
        self.provider = provider
        self.model = model
        if provider == "openai":
            from semantic_seo.shared.api_clients.openai_client import OpenAIClient

            self.client = OpenAIClient(default_model=model)
        else:
            from semantic_seo.shared.api_clients.anthropic_client import AnthropicClient

            self.client = AnthropicClient(default_model=model)

    def run(self, context: DecisionContext) -> LLMTestResult:
        sys, user = generate_conversation_prompts(context)
        if self.provider == "openai":
            output = self.client.generate(user, system=sys)  # type: ignore[union-attr]
        else:
            output = self.client.generate(user, system=sys)  # type: ignore[union-attr]
        return LLMTestResult(provider=self.provider, model=self.model or "default", output=output)
