from __future__ import annotations

from typing import List, Optional

from semantic_seo.shared.utils.logging import get_logger

_logger = get_logger(__name__)

try:
    from google.cloud import language_v1  # type: ignore
except Exception:  # pragma: no cover - optional dependency
    language_v1 = None  # type: ignore


class GoogleNLPClient:
    """Wrapper for Google Cloud Natural Language API entity extraction."""

    def __init__(self) -> None:
        if language_v1 is None:
            _logger.warning("google-cloud-language not installed; GoogleNLPClient is disabled.")
            self.client = None
        else:
            self.client = language_v1.LanguageServiceClient()

    def extract_entities(self, text: str, *, language: str = "en") -> List[dict]:
        if self.client is None:
            raise RuntimeError("GoogleNLPClient unavailable; install google-cloud-language and set credentials")

        document = language_v1.Document(content=text, type_=language_v1.Document.Type.PLAIN_TEXT, language=language)
        response = self.client.analyze_entities(document=document)
        results = []
        for entity in response.entities:
            results.append(
                {
                    "name": entity.name,
                    "type": language_v1.Entity.Type(entity.type_).name,
                    "salience": entity.salience,
                    "metadata": dict(entity.metadata),
                    "mentions": [
                        {
                            "text": m.text.content,
                            "type": language_v1.EntityMention.Type(m.type_).name,
                        }
                        for m in entity.mentions
                    ],
                }
            )
        return results
