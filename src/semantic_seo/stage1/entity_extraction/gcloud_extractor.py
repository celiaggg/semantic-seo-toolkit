from __future__ import annotations

from typing import List, Dict

from semantic_seo.shared.api_clients.google_nlp import GoogleNLPClient


class GoogleEntityExtractor:
    """Named entity extraction using Google Cloud Natural Language API."""

    def __init__(self) -> None:
        self.client = GoogleNLPClient()

    def extract(self, text: str) -> List[Dict[str, object]]:
        return self.client.extract_entities(text)
