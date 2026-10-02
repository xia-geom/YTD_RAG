"""Dataclass models and JSON conversion for the local RAG pipeline.

Types document the index schema; model construction does not coerce or validate
values. The same models are used with every optional dependency combination.
"""

from __future__ import annotations

from dataclasses import asdict, dataclass, field, fields, is_dataclass
from typing import Any, Literal


DocumentType = Literal[
    "paper",
    "note",
    "draft",
    "lecture_note",
    "bibtex",
    "markdown",
    "other",
]
DocumentStatus = Literal["unread", "skimmed", "read", "important"]
ChunkType = Literal[
    "definition",
    "theorem",
    "lemma",
    "proposition",
    "proof",
    "example",
    "computation",
    "remark",
    "question",
    "conjecture",
    "citation_context",
    "text",
]


@dataclass
class DocumentMetadata:
    source_path: str
    title: str | None = None
    authors: list[str] = field(default_factory=list)
    year: int | None = None
    document_type: DocumentType = "other"
    topics: list[str] = field(default_factory=list)
    mathematical_objects: list[str] = field(default_factory=list)
    status: DocumentStatus = "unread"
    notes: str | None = None


@dataclass
class Chunk:
    chunk_id: str
    source_path: str
    title: str | None = None
    chunk_type: ChunkType = "text"
    section_path: list[str] = field(default_factory=list)
    page_number: int | None = None
    line_start: int | None = None
    line_end: int | None = None
    content: str = ""
    metadata: dict[str, Any] = field(default_factory=dict)
    symbols: list[str] = field(default_factory=list)
    topics: list[str] = field(default_factory=list)


@dataclass
class SearchResult:
    chunk: Chunk
    score: float
    keyword_score: float = 0.0
    vector_score: float = 0.0
    rank: int | None = None


_CHUNK_FIELDS = frozenset(item.name for item in fields(Chunk))
_METADATA_FIELDS = frozenset(item.name for item in fields(DocumentMetadata))


def model_to_dict(model: Any) -> dict[str, Any]:
    """Return a plain dict for a dataclass instance or existing dictionary."""

    if is_dataclass(model):
        return asdict(model)
    if isinstance(model, dict):
        return dict(model)
    raise TypeError(f"Cannot serialize object of type {type(model)!r}")


def chunk_from_dict(data: dict[str, Any]) -> Chunk:
    """Read an index record, ignoring unknown fields from other versions."""

    return Chunk(**{key: value for key, value in data.items() if key in _CHUNK_FIELDS})


def metadata_from_dict(data: dict[str, Any]) -> DocumentMetadata:
    """Read known metadata fields while allowing extra keys in source YAML."""

    return DocumentMetadata(**{key: value for key, value in data.items() if key in _METADATA_FIELDS})
