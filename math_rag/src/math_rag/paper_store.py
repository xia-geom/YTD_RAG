"""Storage helpers for discovered and downloaded papers."""

from __future__ import annotations

import json
import re
from dataclasses import asdict, dataclass, field, is_dataclass
from datetime import UTC, datetime
from pathlib import Path
from typing import Any


DEFAULT_CANDIDATES_PATH = "discovered_papers.yaml"
DEFAULT_ARXIV_CORPUS_DIR = "corpus/arxiv"


@dataclass
class PaperCandidate:
    arxiv_id: str
    version: str | None
    title: str
    authors: list[str]
    year: int | None
    arxiv_categories: list[str]
    abstract: str
    score: float = 0.0
    ranking_reasons: list[str] = field(default_factory=list)
    status: str = "pending"
    action: str = "pending"
    source_url: str | None = None
    pdf_url: str | None = None


@dataclass
class DownloadResult:
    arxiv_id: str
    version: str | None
    status: str
    path: str | None = None
    source_downloaded: bool = False
    pdf_downloaded: bool = False
    duplicate: bool = False
    errors: list[str] = field(default_factory=list)


def utc_now_iso() -> str:
    return datetime.now(UTC).replace(microsecond=0).isoformat()


def candidate_from_dict(data: dict[str, Any]) -> PaperCandidate:
    return PaperCandidate(
        arxiv_id=str(data.get("arxiv_id", "")),
        version=data.get("version"),
        title=str(data.get("title", "")),
        authors=list(data.get("authors") or []),
        year=data.get("year"),
        arxiv_categories=list(data.get("arxiv_categories") or []),
        abstract=str(data.get("abstract", "")),
        score=float(data.get("score", 0.0) or 0.0),
        ranking_reasons=list(data.get("ranking_reasons") or []),
        status=str(data.get("status", "pending")),
        action=str(data.get("action", "pending")),
        source_url=data.get("source_url"),
        pdf_url=data.get("pdf_url"),
    )


def candidate_to_dict(candidate: PaperCandidate) -> dict[str, Any]:
    data = _to_dict(candidate)
    data["score"] = round(float(data.get("score", 0.0)), 4)
    return data


def _to_dict(value: Any) -> Any:
    if is_dataclass(value):
        return asdict(value)
    if hasattr(value, "model_dump"):
        return value.model_dump()
    if isinstance(value, dict):
        return {key: _to_dict(item) for key, item in value.items()}
    if isinstance(value, list):
        return [_to_dict(item) for item in value]
    return value


def load_yaml_file(path: str | Path) -> dict[str, Any]:
    file_path = Path(path)
    if not file_path.exists():
        return {}
    text = file_path.read_text(encoding="utf-8")
    try:
        import yaml  # type: ignore

        loaded = yaml.safe_load(text)
        return loaded if isinstance(loaded, dict) else {}
    except Exception:
        try:
            loaded = json.loads(text)
            return loaded if isinstance(loaded, dict) else {}
        except json.JSONDecodeError:
            return _parse_minimal_candidates_yaml(text)


def write_yaml_file(path: str | Path, data: dict[str, Any]) -> None:
    file_path = Path(path)
    file_path.parent.mkdir(parents=True, exist_ok=True) if file_path.parent != Path(".") else None
    try:
        import yaml  # type: ignore

        file_path.write_text(
            yaml.safe_dump(data, sort_keys=False, allow_unicode=True, width=100),
            encoding="utf-8",
        )
    except Exception:
        # JSON is valid YAML and keeps this project usable without pyyaml.
        file_path.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")


def load_candidates(path: str | Path) -> list[PaperCandidate]:
    data = load_yaml_file(path)
    return [candidate_from_dict(item) for item in data.get("candidates", []) if isinstance(item, dict)]


def write_candidates(path: str | Path, candidates: list[PaperCandidate]) -> None:
    write_yaml_file(path, {"candidates": [candidate_to_dict(candidate) for candidate in candidates]})


def approved_candidates(candidates: list[PaperCandidate], auto_download: bool = False, limit: int | None = None) -> list[PaperCandidate]:
    selected = [candidate for candidate in candidates if candidate.action == "download"]
    if auto_download:
        selected.extend(candidate for candidate in candidates if candidate.action == "pending" and candidate not in selected)
    if limit is not None:
        selected = selected[:limit]
    return selected


def safe_arxiv_dirname(arxiv_id: str) -> str:
    cleaned = re.sub(r"[^A-Za-z0-9._-]+", "_", arxiv_id.strip())
    return cleaned or "unknown"


def paper_dir(corpus_arxiv_dir: str | Path, arxiv_id: str) -> Path:
    return Path(corpus_arxiv_dir) / safe_arxiv_dirname(arxiv_id)


def metadata_path(corpus_arxiv_dir: str | Path, arxiv_id: str) -> Path:
    return paper_dir(corpus_arxiv_dir, arxiv_id) / "metadata.yaml"


def is_duplicate(candidate: PaperCandidate, corpus_arxiv_dir: str | Path) -> bool:
    path = metadata_path(corpus_arxiv_dir, candidate.arxiv_id)
    if not path.exists():
        return False
    existing = load_yaml_file(path)
    return existing.get("arxiv_id") == candidate.arxiv_id and existing.get("version") == candidate.version


def build_paper_metadata(
    candidate: PaperCandidate,
    source_available: bool,
    pdf_available: bool,
    primary_ingestion: str,
    topics: list[str] | None = None,
) -> dict[str, Any]:
    return {
        "arxiv_id": candidate.arxiv_id,
        "version": candidate.version,
        "title": candidate.title,
        "authors": candidate.authors,
        "year": candidate.year,
        "abstract": candidate.abstract,
        "arxiv_categories": candidate.arxiv_categories,
        "discovery_score": round(candidate.score, 4),
        "ranking_reasons": list(candidate.ranking_reasons),
        "candidate_status": candidate.status,
        "candidate_action": candidate.action,
        "downloaded_at": utc_now_iso(),
        "source_available": source_available,
        "pdf_available": pdf_available,
        "primary_ingestion": primary_ingestion,
        "topics": topics or [],
        "source_url": candidate.source_url,
        "pdf_url": candidate.pdf_url,
    }


def write_paper_metadata(corpus_arxiv_dir: str | Path, candidate: PaperCandidate, metadata: dict[str, Any]) -> Path:
    path = metadata_path(corpus_arxiv_dir, candidate.arxiv_id)
    write_yaml_file(path, metadata)
    return path


def _parse_minimal_candidates_yaml(text: str) -> dict[str, Any]:
    """Best-effort fallback for manually edited candidate files without pyyaml.

    This is intentionally narrow. Normal installs use pyyaml; this fallback
    handles the generated candidate format well enough to recover actions.
    """

    candidates: list[dict[str, Any]] = []
    current: dict[str, Any] | None = None
    list_key: str | None = None
    for raw_line in text.splitlines():
        line = raw_line.rstrip()
        stripped = line.strip()
        if not stripped or stripped.startswith("#"):
            continue
        if stripped.startswith("- "):
            item = stripped[2:]
            if ":" in item:
                current = {}
                candidates.append(current)
                key, value = item.split(":", 1)
                current[key.strip()] = _parse_scalar(value.strip())
                list_key = None
            elif current is not None and list_key:
                current.setdefault(list_key, []).append(_parse_scalar(item))
            continue
        if current is None:
            continue
        if raw_line.startswith("    - ") and list_key:
            current.setdefault(list_key, []).append(_parse_scalar(stripped[2:].strip()))
            continue
        if ":" in stripped:
            key, value = stripped.split(":", 1)
            key = key.strip()
            value = value.strip()
            if value:
                current[key] = _parse_scalar(value)
                list_key = None
            else:
                current[key] = []
                list_key = key
    return {"candidates": candidates}


def _parse_scalar(value: str) -> Any:
    if value in {"null", "None", "~"}:
        return None
    if value in {"true", "false"}:
        return value == "true"
    if value.startswith('"') and value.endswith('"'):
        return value[1:-1]
    if value.startswith("'") and value.endswith("'"):
        return value[1:-1]
    try:
        if "." in value:
            return float(value)
        return int(value)
    except ValueError:
        return value
