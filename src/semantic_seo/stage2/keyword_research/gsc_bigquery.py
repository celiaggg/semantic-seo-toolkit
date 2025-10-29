from __future__ import annotations

from typing import List, Dict

from semantic_seo.shared.utils.logging import get_logger

_logger = get_logger(__name__)

try:
    from google.cloud import bigquery  # type: ignore
except Exception:  # pragma: no cover
    bigquery = None  # type: ignore


def run_bigquery(sql: str, *, project: str | None = None) -> List[Dict[str, object]]:
    """Run a BigQuery SQL query and return rows as dicts."""
    if bigquery is None:
        raise RuntimeError("google-cloud-bigquery not installed")
    client = bigquery.Client(project=project)
    job = client.query(sql)
    rows = list(job.result())
    return [dict(row.items()) for row in rows]


def fetch_gsc_queries(table_fqn: str, *, limit: int = 1000, project: str | None = None) -> List[Dict[str, object]]:
    """Example: SELECT top queries from a Search Console export in BigQuery."""
    sql = f"""
    SELECT query, SUM(clicks) AS clicks, SUM(impressions) AS impressions
    FROM `{table_fqn}`
    GROUP BY query
    ORDER BY impressions DESC
    LIMIT {int(limit)}
    """
    _logger.info("Running BigQuery for GSC table: %s", table_fqn)
    return run_bigquery(sql, project=project)
