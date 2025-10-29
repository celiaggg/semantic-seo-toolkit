"""Semantic SEO Toolkit

Modular pipeline for persona-driven prompt engineering, entity extraction,
classification, gap analysis, and content optimization.
"""

from importlib.metadata import version

__all__ = [
    "version",
]

try:
    __version__ = version("semantic-seo")
except Exception:
    __version__ = "0.1.0"
