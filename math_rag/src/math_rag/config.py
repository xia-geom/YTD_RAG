"""Configuration helpers.

Defaults are intentionally local-only. Remote embedding or LLM providers should
be added behind explicit opt-in settings later.
"""

from __future__ import annotations

import os
from dataclasses import dataclass
from pathlib import Path


DEFAULT_INDEX_DIR = ".math_rag_index"
SUPPORTED_SUFFIXES = {".tex", ".md", ".markdown", ".txt", ".bib", ".pdf"}


@dataclass(frozen=True)
class Settings:
    index_dir: Path = Path(DEFAULT_INDEX_DIR)
    embedding_backend: str = "local"
    local_only: bool = True


def load_settings(index_dir: str | Path | None = None) -> Settings:
    env_index = os.getenv("MATH_RAG_INDEX_DIR")
    env_backend = os.getenv("MATH_RAG_EMBEDDING_BACKEND", "local")
    env_local_only = os.getenv("MATH_RAG_LOCAL_ONLY", "true").lower()
    return Settings(
        index_dir=Path(index_dir or env_index or DEFAULT_INDEX_DIR),
        embedding_backend=env_backend,
        local_only=env_local_only not in {"0", "false", "no"},
    )

