"""Structured data models used by the local RAG pipeline.

The project uses pydantic when it is installed. A small dataclass fallback keeps
the first version runnable in bare Python environments, which is useful for a
private local-first tool.
"""

from __future__ import annotations

from dataclasses import asdict, dataclass, field, is_dataclass
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


try:  # pragma: no cover - exercised only when pydantic is installed
    from pydantic import BaseModel, Field

    class DocumentMetadata(BaseModel):
        source_path: str
        title: str | None = None
        authors: list[str] = Field(default_factory=list)
        year: int | None = None
        document_type: DocumentType = "other"
        topics: list[str] = Field(default_factory=list)
        mathematical_objects: list[str] = Field(default_factory=list)
        status: DocumentStatus = "unread"
        notes: str | None = None

    class Chunk(BaseModel):
        chunk_id: str
        source_path: str
        title: str | None = None
        chunk_type: ChunkType = "text"
        section_path: list[str] = Field(default_factory=list)
        page_number: int | None = None
        line_start: int | None = None
        line_end: int | None = None
        content: str
        metadata: dict[str, Any] = Field(default_factory=dict)
        symbols: list[str] = Field(default_factory=list)
        topics: list[str] = Field(default_factory=list)

    class SearchResult(BaseModel):
        chunk: Chunk
        score: float
        keyword_score: float = 0.0
        vector_score: float = 0.0
        rank: int | None = None

except Exception:  # pragma: no cover - main path in the execution sandbox

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


def model_to_dict(model: Any) -> dict[str, Any]:
    """Return a plain dict for pydantic or dataclass model instances."""

    if hasattr(model, "model_dump"):
        return model.model_dump()
    if is_dataclass(model):
        return asdict(model)
    if isinstance(model, dict):
        return dict(model)
    raise TypeError(f"Cannot serialize object of type {type(model)!r}")


def chunk_from_dict(data: dict[str, Any]) -> Chunk:
    return Chunk(**data)


def metadata_from_dict(data: dict[str, Any]) -> DocumentMetadata:
    return DocumentMetadata(**data)

