from __future__ import annotations

import re
from typing import Iterable, List

try:
    from bs4 import BeautifulSoup  # type: ignore
except Exception:  # pragma: no cover - optional dependency
    BeautifulSoup = None  # type: ignore


_whitespace_re = re.compile(r"\s+")


def normalize_whitespace(text: str) -> str:
    """Collapse and trim whitespace."""
    return _whitespace_re.sub(" ", text).strip()


def strip_html(text: str) -> str:
    """Remove HTML tags if BeautifulSoup is available; otherwise naive strip."""
    if BeautifulSoup is None:
        return re.sub(r"<[^>]+>", " ", text)
    soup = BeautifulSoup(text, "html.parser")
    return normalize_whitespace(soup.get_text(separator=" "))


def dedupe_keep_order(items: Iterable[str]) -> List[str]:
    seen = set()
    out: List[str] = []
    for item in items:
        if item not in seen:
            out.append(item)
            seen.add(item)
    return out
