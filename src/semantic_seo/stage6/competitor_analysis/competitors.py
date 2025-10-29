from __future__ import annotations

from typing import List, Dict

import trafilatura


def fetch_and_extract(urls: List[str]) -> List[Dict[str, str]]:
    """Download and extract main text content for competitor pages."""
    results: List[Dict[str, str]] = []
    for url in urls:
        downloaded = trafilatura.fetch_url(url)
        text = trafilatura.extract(downloaded) if downloaded else None
        results.append({"url": url, "text": text or ""})
    return results
