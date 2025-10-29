from __future__ import annotations

from typing import Dict, List, Optional

import os
import requests


def fetch_semrush_keywords(domain: str, *, api_key: Optional[str] = None, limit: int = 100) -> List[Dict[str, object]]:
    """Fetch keywords using SEMrush API (illustrative placeholder).

    Note: Replace with the correct SEMrush endpoint and parameters for your subscription.
    """
    key = api_key or os.getenv("SEMRUSH_API_KEY")
    if not key:
        raise RuntimeError("SEMRUSH_API_KEY is not set")
    # Placeholder endpoint; update to match actual SEMrush API
    url = "https://api.semrush.com/keywords/v1/domain"
    params = {"key": key, "domain": domain, "limit": limit}
    resp = requests.get(url, params=params, timeout=30)
    resp.raise_for_status()
    data = resp.json()
    return data if isinstance(data, list) else []
