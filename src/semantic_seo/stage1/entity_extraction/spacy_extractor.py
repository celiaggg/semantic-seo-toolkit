from __future__ import annotations

from typing import List, Dict

from semantic_seo.shared.utils.logging import get_logger

_logger = get_logger(__name__)

try:
    import spacy  # type: ignore
except Exception:  # pragma: no cover - optional dependency
    spacy = None  # type: ignore


class SpacyEntityExtractor:
    """Named entity extraction using spaCy."""

    def __init__(self, model: str = "en_core_web_md") -> None:
        if spacy is None:
            raise RuntimeError("spaCy is not installed. Add it to requirements and install a model.")
        try:
            self.nlp = spacy.load(model)
        except OSError:
            _logger.error("spaCy model '%s' not installed. Run: python -m spacy download %s", model, model)
            raise

    def extract(self, text: str) -> List[Dict[str, str]]:
        doc = self.nlp(text)
        entities: List[Dict[str, str]] = []
        for ent in doc.ents:
            entities.append({"text": ent.text, "label": ent.label_})
        return entities
