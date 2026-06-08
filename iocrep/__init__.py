"""IOCREP — offline IOC reputation scoring with explainable verdicts.

Score indicators of compromise (IPs, domains, URLs, file hashes, emails)
against offline reputation feeds and allow lists. Defensive triage only:
no network calls, no active enumeration, purely local artifact analysis.
"""
from .core import (
    Indicator,
    Verdict,
    ReputationDB,
    classify_indicator,
    score_indicator,
    score_batch,
)

TOOL_NAME = "iocrep"
TOOL_VERSION = "1.0.0"

__all__ = [
    "Indicator",
    "Verdict",
    "ReputationDB",
    "classify_indicator",
    "score_indicator",
    "score_batch",
    "TOOL_NAME",
    "TOOL_VERSION",
]
