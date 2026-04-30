"""Retrieval-only evaluation helpers for math_rag."""

from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

from .config import DEFAULT_INDEX_DIR, load_settings
from .hybrid_search import search_chunks
from .index_store import IndexStore
from .models import Chunk, SearchResult
from .rag_service import IndexNotFoundError


DEFAULT_HITS_AT = (1, 3, 5)


@dataclass(frozen=True)
class GoldQuestion:
    question_id: str
    question: str
    expected_sources: list[str] = field(default_factory=list)
    negative: bool = False
    notes: str | None = None


@dataclass(frozen=True)
class EvalRow:
    question_id: str
    question: str
    hit: bool | None
    first_expected_rank: int | None
    expected_sources: list[str]
    top_sources: list[str]
    negative: bool = False
    missing_expected_sources: list[str] = field(default_factory=list)


def load_gold_questions(eval_path: str | Path) -> list[GoldQuestion]:
    """Load a YAML retrieval-eval file.

    Expected shape:

    ``questions`` may be a list of mappings with ``id``, ``question``,
    ``expected_sources``, and optional ``negative``. A top-level list is also
    accepted for small fixtures.
    """

    try:
        import yaml  # type: ignore
    except Exception as exc:  # pragma: no cover - dependency declared in pyproject
        raise RuntimeError("PyYAML is required to load eval YAML files.") from exc

    path = Path(eval_path)
    raw = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    items = raw.get("questions", raw) if isinstance(raw, dict) else raw
    if not isinstance(items, list):
        raise ValueError("Eval YAML must contain a questions list.")

    questions: list[GoldQuestion] = []
    seen_ids: set[str] = set()
    for index, item in enumerate(items, start=1):
        if not isinstance(item, dict):
            raise ValueError(f"Question entry {index} must be a mapping.")
        question = item.get("question") or item.get("query")
        if not isinstance(question, str) or not question.strip():
            raise ValueError(f"Question entry {index} is missing a non-empty question.")
        question_id = str(item.get("id") or f"q{index:03d}").strip()
        if not question_id:
            raise ValueError(f"Question entry {index} has an empty id.")
        if question_id in seen_ids:
            raise ValueError(f"Duplicate question id: {question_id}")
        seen_ids.add(question_id)

        expected_raw = item.get("expected_sources", [])
        if expected_raw is None:
            expected_raw = []
        if not isinstance(expected_raw, list) or not all(isinstance(value, str) for value in expected_raw):
            raise ValueError(f"Question {question_id} expected_sources must be a list of strings.")
        negative = bool(item.get("negative", False))
        if not negative and not expected_raw:
            raise ValueError(f"Question {question_id} must have expected_sources or negative: true.")
        notes = item.get("notes")
        questions.append(
            GoldQuestion(
                question_id=question_id,
                question=question.strip(),
                expected_sources=[value.strip() for value in expected_raw if value.strip()],
                negative=negative,
                notes=str(notes) if notes is not None else None,
            )
        )
    return questions


def evaluate_retrieval(
    eval_path: str | Path,
    *,
    index_dir: str = DEFAULT_INDEX_DIR,
    mode: str = "hybrid",
    top_k: int = 5,
    hits_at: tuple[int, ...] = DEFAULT_HITS_AT,
) -> dict[str, Any]:
    questions = load_gold_questions(eval_path)
    store = IndexStore(index_dir)
    chunks = store.load_chunks()
    if not chunks:
        raise IndexNotFoundError(
            f"No index found or index is empty at {store.index_path}. "
            "Run: python -m math_rag.cli ingest corpus/"
        )

    hits_at = tuple(sorted(set(int(k) for k in hits_at if int(k) > 0))) or DEFAULT_HITS_AT
    top_k = max(int(top_k), max(hits_at))
    settings = load_settings(index_dir)

    rows: list[EvalRow] = []
    for question in questions:
        retrieval_k = max(top_k * 4, 20)
        results = search_chunks(
            chunks,
            question.question,
            mode=mode,
            top_k=retrieval_k,
            vector_backend=settings.embedding_backend,
        )
        first_rank = _first_expected_source_rank(results, question.expected_sources)
        missing = [
            expected
            for expected in question.expected_sources
            if not _expected_source_in_chunks(chunks, expected)
        ]
        rows.append(
            EvalRow(
                question_id=question.question_id,
                question=question.question,
                hit=None if question.negative else first_rank is not None,
                first_expected_rank=first_rank,
                expected_sources=list(question.expected_sources),
                top_sources=_unique_source_paths(results, limit=top_k),
                negative=question.negative,
                missing_expected_sources=missing,
            )
        )

    positive_rows = [row for row in rows if not row.negative]
    hits_summary: dict[int, dict[str, int | float]] = {}
    for k in hits_at:
        hits = sum(
            1
            for row in positive_rows
            if row.first_expected_rank is not None and row.first_expected_rank <= k
        )
        total = len(positive_rows)
        hits_summary[k] = {
            "hits": hits,
            "total": total,
            "rate": hits / total if total else 0.0,
        }

    max_k = max(hits_at)
    worst_failures = [
        row_to_dict(row)
        for row in positive_rows
        if row.first_expected_rank is None or row.first_expected_rank > max_k
    ]
    missing_expected_sources = sorted({source for row in rows for source in row.missing_expected_sources})

    return {
        "eval_path": str(eval_path),
        "index_dir": index_dir,
        "mode": mode,
        "top_k": top_k,
        "total_questions": len(rows),
        "evaluated_questions": len(positive_rows),
        "negative_questions": sum(1 for row in rows if row.negative),
        "hits_at": hits_summary,
        "missing_expected_sources": missing_expected_sources,
        "worst_failures": worst_failures,
        "rows": [row_to_dict(row) for row in rows],
    }


def row_to_dict(row: EvalRow) -> dict[str, Any]:
    return {
        "question_id": row.question_id,
        "question": row.question,
        "hit": row.hit,
        "first_expected_rank": row.first_expected_rank,
        "expected_sources": list(row.expected_sources),
        "top_sources": list(row.top_sources),
        "negative": row.negative,
        "missing_expected_sources": list(row.missing_expected_sources),
    }


def format_eval_report(summary: dict[str, Any]) -> str:
    lines = [
        "Question ID | Hit? | First expected rank | Expected sources | Top sources",
        "--- | --- | --- | --- | ---",
    ]
    for row in summary["rows"]:
        if row["negative"]:
            hit = "negative"
        else:
            hit = "yes" if row["hit"] else "no"
        rank = str(row["first_expected_rank"]) if row["first_expected_rank"] is not None else "-"
        expected = ", ".join(row["expected_sources"]) if row["expected_sources"] else "-"
        top_sources = ", ".join(row["top_sources"]) if row["top_sources"] else "-"
        lines.append(f"{row['question_id']} | {hit} | {rank} | {expected} | {top_sources}")

    lines.extend(
        [
            "",
            f"Total questions: {summary['total_questions']}",
            f"Evaluated positive questions: {summary['evaluated_questions']}",
            f"Negative questions: {summary['negative_questions']}",
        ]
    )
    for k, values in summary["hits_at"].items():
        lines.append(f"hits@{k}: {values['hits']}/{values['total']} = {values['rate']:.3f}")

    lines.append("Missing expected sources:")
    if summary["missing_expected_sources"]:
        for source in summary["missing_expected_sources"]:
            lines.append(f"- {source}")
    else:
        lines.append("- none")

    lines.append("Worst failures:")
    if summary["worst_failures"]:
        for row in summary["worst_failures"][:10]:
            expected = ", ".join(row["expected_sources"]) if row["expected_sources"] else "-"
            top_sources = ", ".join(row["top_sources"][:5]) if row["top_sources"] else "-"
            lines.append(f"- {row['question_id']}: expected {expected}; top {top_sources}")
    else:
        lines.append("- none")
    return "\n".join(lines)


def _first_expected_source_rank(results: list[SearchResult], expected_sources: list[str]) -> int | None:
    if not expected_sources:
        return None
    seen_sources: set[str] = set()
    source_rank = 0
    for result in results:
        source_path = result.chunk.source_path
        if source_path in seen_sources:
            continue
        seen_sources.add(source_path)
        source_rank += 1
        if any(_result_matches_expected_source(result, expected) for expected in expected_sources):
            return source_rank
    return None


def _unique_source_paths(results: list[SearchResult], limit: int) -> list[str]:
    seen_sources: set[str] = set()
    sources: list[str] = []
    for result in results:
        source_path = result.chunk.source_path
        if source_path in seen_sources:
            continue
        seen_sources.add(source_path)
        sources.append(source_path)
        if len(sources) >= limit:
            break
    return sources


def _expected_source_in_chunks(chunks: list[Chunk], expected: str) -> bool:
    return any(_chunk_matches_expected_source(chunk, expected) for chunk in chunks)


def _result_matches_expected_source(result: SearchResult, expected: str) -> bool:
    return _chunk_matches_expected_source(result.chunk, expected)


def _chunk_matches_expected_source(chunk: Chunk, expected: str) -> bool:
    expected_key = _normalize_source_key(expected)
    if not expected_key:
        return False
    return any(expected_key in key for key in _chunk_source_keys(chunk))


def _chunk_source_keys(chunk: Chunk) -> set[str]:
    keys = {_normalize_source_key(chunk.source_path)}
    for name in ("arxiv_id", "requested_arxiv_id", "arxiv_version", "pdf_url", "source_url"):
        value = chunk.metadata.get(name)
        if value:
            keys.add(_normalize_source_key(str(value)))
    return {key for key in keys if key}


def _normalize_source_key(value: str) -> str:
    return value.strip().lower().replace("\\", "/").replace("/", "_")
