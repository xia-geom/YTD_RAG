"""Simple local JSON index store."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from .config import DEFAULT_INDEX_DIR
from .models import Chunk, chunk_from_dict, model_to_dict


INDEX_FILENAME = "index.json"


class IndexStore:
    def __init__(self, index_dir: str | Path = DEFAULT_INDEX_DIR):
        self.index_dir = Path(index_dir)
        self.index_path = self.index_dir / INDEX_FILENAME

    def exists(self) -> bool:
        return self.index_path.exists()

    def save_chunks(self, chunks: list[Chunk]) -> None:
        self.index_dir.mkdir(parents=True, exist_ok=True)
        payload: dict[str, Any] = {
            "schema_version": 1,
            "chunks": [model_to_dict(chunk) for chunk in chunks],
        }
        self.index_path.write_text(json.dumps(payload, indent=2, ensure_ascii=False), encoding="utf-8")

    def load_chunks(self) -> list[Chunk]:
        if not self.index_path.exists():
            return []
        payload = json.loads(self.index_path.read_text(encoding="utf-8"))
        return [chunk_from_dict(item) for item in payload.get("chunks", [])]

    def stats(self) -> dict[str, Any]:
        chunks = self.load_chunks()
        sources = {chunk.source_path for chunk in chunks}
        by_type: dict[str, int] = {}
        for chunk in chunks:
            by_type[chunk.chunk_type] = by_type.get(chunk.chunk_type, 0) + 1
        return {
            "index_path": str(self.index_path),
            "chunk_count": len(chunks),
            "source_count": len(sources),
            "chunk_types": by_type,
        }

