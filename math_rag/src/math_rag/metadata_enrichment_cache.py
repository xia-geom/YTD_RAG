"""Local cache for metadata-only chunk enrichment."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any

from .metadata_enrichment import ENRICHMENT_BACKEND, ENRICHMENT_VERSION, PROMPT_HASH, enrich_chunk
from .models import Chunk, DocumentMetadata, model_to_dict


BASE_CHUNKER_VERSION = "deterministic_chunker_v1"
ENRICHMENT_CACHE_DIRNAME = "metadata_enrichment_cache"
ENRICHMENT_METADATA_KEY = "enrichment"


class MetadataEnrichmentCache:
    """Read/write namespaced enrichment metadata keyed by deterministic chunk id."""

    def __init__(self, cache_dir: str | Path):
        self.cache_dir = Path(cache_dir)
        self.files_dir = self.cache_dir / "files"

    def apply(
        self,
        source_path: str | Path,
        metadata: DocumentMetadata,
        chunks: list[Chunk],
        *,
        refresh: bool = False,
    ) -> None:
        """Apply cached or newly computed enrichment metadata to chunks."""

        path = Path(source_path)
        expected = self._cache_header(path, metadata)
        cached = None if refresh else self._read_cache(path)
        if cached and self._is_compatible(cached, expected):
            enrichments = cached.get("enrichments_by_chunk_id")
            if isinstance(enrichments, dict):
                self._merge_enrichments(chunks, enrichments)
                return

        enrichments = {chunk.chunk_id: enrich_chunk(chunk) for chunk in chunks}
        self._merge_enrichments(chunks, enrichments)
        self._write_cache(path, {**expected, "enrichments_by_chunk_id": enrichments})

    def cache_path_for_source(self, source_path: str | Path) -> Path:
        return self.files_dir / f"{source_path_key(source_path)}.json"

    def _cache_header(self, source_path: Path, metadata: DocumentMetadata) -> dict[str, Any]:
        return {
            "schema_version": 1,
            "source_path": source_path.as_posix(),
            "source_hash": source_hash(source_path),
            "metadata_hash": metadata_hash(metadata),
            "base_chunker_version": BASE_CHUNKER_VERSION,
            "enrichment_version": ENRICHMENT_VERSION,
            "enrichment_backend": ENRICHMENT_BACKEND,
            "prompt_hash": PROMPT_HASH,
        }

    def _read_cache(self, source_path: Path) -> dict[str, Any] | None:
        cache_path = self.cache_path_for_source(source_path)
        if not cache_path.exists():
            return None
        try:
            payload = json.loads(cache_path.read_text(encoding="utf-8"))
        except Exception:
            return None
        return payload if isinstance(payload, dict) else None

    def _write_cache(self, source_path: Path, payload: dict[str, Any]) -> None:
        self.files_dir.mkdir(parents=True, exist_ok=True)
        self.cache_path_for_source(source_path).write_text(
            json.dumps(payload, indent=2, ensure_ascii=False, sort_keys=True),
            encoding="utf-8",
        )
        self._write_manifest()

    def _write_manifest(self) -> None:
        self.cache_dir.mkdir(parents=True, exist_ok=True)
        payload = {
            "schema_version": 1,
            "base_chunker_version": BASE_CHUNKER_VERSION,
            "enrichment_version": ENRICHMENT_VERSION,
            "enrichment_backend": ENRICHMENT_BACKEND,
            "prompt_hash": PROMPT_HASH,
        }
        (self.cache_dir / "manifest.json").write_text(
            json.dumps(payload, indent=2, ensure_ascii=False, sort_keys=True),
            encoding="utf-8",
        )

    @staticmethod
    def _is_compatible(cached: dict[str, Any], expected: dict[str, Any]) -> bool:
        keys = (
            "schema_version",
            "source_path",
            "source_hash",
            "metadata_hash",
            "base_chunker_version",
            "enrichment_version",
            "enrichment_backend",
            "prompt_hash",
        )
        return all(cached.get(key) == expected.get(key) for key in keys)

    @staticmethod
    def _merge_enrichments(chunks: list[Chunk], enrichments: dict[str, Any]) -> None:
        for chunk in chunks:
            enrichment = enrichments.get(chunk.chunk_id)
            if isinstance(enrichment, dict):
                chunk.metadata[ENRICHMENT_METADATA_KEY] = dict(enrichment)


def source_path_key(source_path: str | Path) -> str:
    return hashlib.sha256(Path(source_path).as_posix().encode("utf-8")).hexdigest()[:32]


def source_hash(source_path: str | Path) -> str:
    path = Path(source_path)
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return f"sha256:{digest.hexdigest()}"


def metadata_hash(metadata: DocumentMetadata) -> str:
    payload = json.dumps(model_to_dict(metadata), ensure_ascii=False, sort_keys=True, default=str)
    return f"sha256:{hashlib.sha256(payload.encode('utf-8')).hexdigest()}"
