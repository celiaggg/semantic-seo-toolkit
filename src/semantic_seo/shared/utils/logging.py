from __future__ import annotations

import logging
import sys
from typing import Optional


_LOG_FORMAT = (
    "%(asctime)s | %(levelname)8s | %(name)s | %(message)s"
)


def configure_logging(level: str = "INFO") -> None:
    """Configure root logger with a standard formatter.

    Parameters
    ----------
    level:
        Logging level name, e.g., "DEBUG", "INFO", "WARNING".
    """
    root = logging.getLogger()
    if root.handlers:
        # Avoid duplicate handlers when called multiple times.
        return

    handler = logging.StreamHandler(stream=sys.stdout)
    formatter = logging.Formatter(_LOG_FORMAT)
    handler.setFormatter(formatter)

    root.setLevel(getattr(logging, level.upper(), logging.INFO))
    root.addHandler(handler)


def get_logger(name: Optional[str] = None) -> logging.Logger:
    """Return a module-level logger. Call `configure_logging()` once early.

    Parameters
    ----------
    name:
        Logger name. Defaults to `__name__` of the caller's module.
    """
    return logging.getLogger(name or __name__)
