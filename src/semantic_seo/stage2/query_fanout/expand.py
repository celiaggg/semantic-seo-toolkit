from __future__ import annotations

from typing import List

from semantic_seo.shared.api_clients.openai_client import OpenAIClient


def query_fanout(seed_query: str, *, num_variants: int = 10) -> List[str]:
    """Use an LLM to expand a seed query into variants."""
    client = OpenAIClient()
    prompt = (
        "Generate "
        f"{num_variants} diverse, relevant variations of the following query.\n"
        "Focus on covering attributes like scalability, latency, integration, and cost.\n"
        f"Seed: {seed_query}"
    )
    text = client.generate(prompt)
    lines = [l.strip("- ") for l in text.splitlines() if l.strip()]
    # Deduplicate while preserving order
    seen = set()
    out: List[str] = []
    for l in lines:
        if l not in seen:
            out.append(l)
            seen.add(l)
    return out[:num_variants]
