"""Exploratory inspection for candidate evidence-level eval questions."""

from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

from .citations import format_section_path
from .config import DEFAULT_INDEX_DIR, load_settings
from .eval import _chunk_matches_expected_source
from .hybrid_search import search_chunks
from .index_store import IndexStore
from .models import SearchResult
from .rag_service import IndexNotFoundError
from .text_cleaning import make_snippet, normalize_whitespace


REQUIRED_CANDIDATE_FIELDS = {
    "id",
    "topic",
    "question",
    "expected_sources",
    "expected_chunk_types",
    "expected_terms",
    "preferred_sections",
    "relevance_rubric",
    "review_status",
    "review_notes",
    "correction_needed",
}
VALID_REVIEW_STATUSES = {
    "unreviewed",
    "promote_candidate",
    "needs_correction",
    "needs_corpus_expansion",
    "drop",
    "exploratory_only",
}
STRONG_EVIDENCE_CHUNK_TYPES = {"theorem", "proposition", "definition", "proof", "example"}
FRIENDLY_NOTE_TITLES = {
    "one_conic_point.tex": "CP1 one-conic-point notes",
    "one_cusp_point.tex": "CP1 one-cusp-point notes",
    "notation_table.tex": "Mixed conic/cusp notation table",
    "kenergy_table.tex": "Toric K-energy dictionary table",
    "weighted_twisted.tex": "Weighted twisted Mabuchi notes",
    "project_paper_index.md": "Project paper index",
    "requested_non_arxiv_sources.md": "Requested non-arXiv source pointers",
}


@dataclass(frozen=True)
class CandidateEvidenceQuestion:
    question_id: str
    topic: str
    question: str
    expected_sources: list[str] = field(default_factory=list)
    expected_chunk_types: list[str] = field(default_factory=list)
    expected_terms: list[str] = field(default_factory=list)
    preferred_sections: list[str] = field(default_factory=list)
    relevance_rubric: dict[str, str] = field(default_factory=dict)
    negative: bool = False
    review_status: str = "unreviewed"
    review_notes: str = ""
    correction_needed: str = ""


def load_candidate_evidence_questions(eval_path: str | Path) -> list[CandidateEvidenceQuestion]:
    """Load candidate evidence questions without treating them as gold labels."""

    try:
        import yaml  # type: ignore
    except Exception as exc:  # pragma: no cover - dependency declared in pyproject
        raise RuntimeError("PyYAML is required to load candidate evidence YAML files.") from exc

    path = Path(eval_path)
    raw = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    items = raw.get("questions", raw) if isinstance(raw, dict) else raw
    if not isinstance(items, list):
        raise ValueError("Candidate evidence YAML must contain a questions list.")

    questions: list[CandidateEvidenceQuestion] = []
    seen_ids: set[str] = set()
    for index, item in enumerate(items, start=1):
        if not isinstance(item, dict):
            raise ValueError(f"Candidate question entry {index} must be a mapping.")
        missing = REQUIRED_CANDIDATE_FIELDS - set(item)
        if missing:
            raise ValueError(f"Candidate question entry {index} is missing fields: {', '.join(sorted(missing))}.")

        question_id = _required_string(item, "id", index)
        if question_id in seen_ids:
            raise ValueError(f"Duplicate candidate question id: {question_id}")
        seen_ids.add(question_id)

        questions.append(
            CandidateEvidenceQuestion(
                question_id=question_id,
                topic=_required_string(item, "topic", index),
                question=_required_string(item, "question", index),
                expected_sources=_string_list(item, "expected_sources", question_id),
                expected_chunk_types=_string_list(item, "expected_chunk_types", question_id),
                expected_terms=_string_list(item, "expected_terms", question_id),
                preferred_sections=_string_list(item, "preferred_sections", question_id),
                relevance_rubric=_rubric(item.get("relevance_rubric"), question_id),
                negative=bool(item.get("negative", False)),
                review_status=_review_status(item.get("review_status"), question_id),
                review_notes=_optional_string(item, "review_notes", question_id),
                correction_needed=_optional_string(item, "correction_needed", question_id),
            )
        )
    return questions


def inspect_candidate_evidence_eval(
    eval_path: str | Path,
    *,
    index_dir: str = DEFAULT_INDEX_DIR,
    mode: str = "hybrid",
    top_k: int = 10,
) -> dict[str, Any]:
    """Retrieve top chunks for candidate questions and return diagnostic rows."""

    questions = load_candidate_evidence_questions(eval_path)
    store = IndexStore(index_dir)
    chunks = store.load_chunks()
    if not chunks:
        raise IndexNotFoundError(
            f"No index found or index is empty at {store.index_path}. "
            "Run: python -m math_rag.cli ingest corpus/"
        )

    top_k = max(1, int(top_k))
    settings = load_settings(index_dir)
    rows = []
    for question in questions:
        results = search_chunks(
            chunks,
            question.question,
            mode=mode,
            top_k=top_k,
            vector_backend=settings.embedding_backend,
        )
        result_rows = [_result_to_inspection_row(result, question) for result in results]
        expected_source_seen = any(row["source_matches_expected"] for row in result_rows)
        expected_chunk_type_seen = any(row["chunk_type_matches_expected"] for row in result_rows)
        expected_terms_seen = any(row["matched_expected_terms"] for row in result_rows)
        citation_context_count = sum(1 for row in result_rows if row["chunk_type"] == "citation_context")
        negative_strong_evidence = (
            question.negative
            and any(row["chunk_type"] in STRONG_EVIDENCE_CHUNK_TYPES and row["matched_expected_terms"] for row in result_rows)
        )

        rows.append(
            {
                "id": question.question_id,
                "topic": question.topic,
                "question": question.question,
                "expected_sources": list(question.expected_sources),
                "expected_chunk_types": list(question.expected_chunk_types),
                "expected_terms": list(question.expected_terms),
                "preferred_sections": list(question.preferred_sections),
                "negative": question.negative,
                "review_status": question.review_status,
                "review_notes": question.review_notes,
                "correction_needed": question.correction_needed,
                "diagnostics": {
                    "expected_source_in_top_k": expected_source_seen,
                    "expected_chunk_type_in_top_k": expected_chunk_type_seen,
                    "expected_terms_in_top_k": expected_terms_seen,
                    "citation_context_in_top_k_count": citation_context_count,
                    "negative_strong_evidence_manual_review_needed": negative_strong_evidence,
                },
                "top_chunks": result_rows,
            }
        )

    return {
        "eval_path": str(eval_path),
        "index_dir": index_dir,
        "mode": mode,
        "top_k": top_k,
        "total_questions": len(rows),
        "negative_questions": sum(1 for row in rows if row["negative"]),
        "rows": rows,
    }


def format_candidate_evidence_inspection_markdown(report: dict[str, Any]) -> str:
    """Format a human-review Markdown inspection report."""

    lines = [
        "# Candidate Evidence Eval Inspection",
        "",
        "> Exploratory diagnostic report only. Do not treat these counts as regression metrics.",
        "",
        f"- Eval file: `{report['eval_path']}`",
        f"- Index dir: `{report['index_dir']}`",
        f"- Mode: `{report['mode']}`",
        f"- Top-k: `{report['top_k']}`",
        f"- Candidate questions: {report['total_questions']}",
        f"- Negative questions: {report['negative_questions']}",
        "",
        "## Diagnostic Counts",
        "",
        f"- Expected source appeared in top-k: {_count_true(report['rows'], 'expected_source_in_top_k')}/{report['total_questions']}",
        f"- Expected chunk type appeared in top-k: {_count_true(report['rows'], 'expected_chunk_type_in_top_k')}/{report['total_questions']}",
        f"- Expected terms appeared in top-k: {_count_true(report['rows'], 'expected_terms_in_top_k')}/{report['total_questions']}",
        (
            "- Negative questions with strong-looking evidence requiring manual review: "
            f"{_count_true(report['rows'], 'negative_strong_evidence_manual_review_needed')}"
        ),
        "",
        "## Questions",
        "",
    ]

    for row in report["rows"]:
        diagnostics = row["diagnostics"]
        lines.extend(
            [
                f"### {row['id']} - {row['topic']}",
                "",
                f"**Question:** {row['question']}",
                "",
                f"**Expected sources:** {_format_list(row['expected_sources'])}",
                f"**Expected chunk types:** {_format_list(row['expected_chunk_types'])}",
                f"**Expected terms:** {_format_list(row['expected_terms'])}",
                f"**Preferred sections:** {_format_list(row['preferred_sections'])}",
                f"**Negative:** {'yes' if row['negative'] else 'no'}",
                f"**Review status:** `{row['review_status']}`",
                f"**Review notes:** {row['review_notes'] or '-'}",
                f"**Correction needed:** {row['correction_needed'] or '-'}",
                "",
                "**Diagnostics:**",
                f"- Expected source in top-k: {_yes_no(diagnostics['expected_source_in_top_k'])}",
                f"- Expected chunk type in top-k: {_yes_no(diagnostics['expected_chunk_type_in_top_k'])}",
                f"- Expected terms in top-k: {_yes_no(diagnostics['expected_terms_in_top_k'])}",
                f"- Citation-context chunks in top-k: {diagnostics['citation_context_in_top_k_count']}",
                (
                    "- Negative strong-looking evidence manual review needed: "
                    f"{_yes_no(diagnostics['negative_strong_evidence_manual_review_needed'])}"
                ),
                "",
                "| Rank | Score | Source | Type | Section | Location | Source? | Type? | Terms | Snippet |",
                "| ---: | ---: | --- | --- | --- | --- | --- | --- | --- | --- |",
            ]
        )
        for chunk_row in row["top_chunks"]:
            lines.append(
                "| {rank} | {score:.3f} | `{source_path}` | `{chunk_type}` | {section_path} | {location} | "
                "{source_match} | {type_match} | {terms} | {snippet} |".format(
                    rank=chunk_row["rank"],
                    score=chunk_row["score"],
                    source_path=_escape_pipes(chunk_row["source_path"]),
                    chunk_type=chunk_row["chunk_type"],
                    section_path=_escape_pipes(chunk_row["section_path"] or "-"),
                    location=_escape_pipes(chunk_row["location"] or "-"),
                    source_match=_yes_no(chunk_row["source_matches_expected"]),
                    type_match=_yes_no(chunk_row["chunk_type_matches_expected"]),
                    terms=_escape_pipes(", ".join(chunk_row["matched_expected_terms"]) or "-"),
                    snippet=_escape_pipes(chunk_row["snippet"]),
                )
            )
        lines.extend(
            [
                "",
                "**Manual relevance notes:**",
                "- rank 1:",
                "- rank 2:",
                "- rank 3:",
                "",
                "Promote to gold? yes/no",
                "",
                "Correction needed:",
                "",
            ]
        )
    return "\n".join(lines).rstrip() + "\n"


def write_candidate_evidence_inspection_markdown(report: dict[str, Any], out_path: str | Path) -> Path:
    path = Path(out_path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(format_candidate_evidence_inspection_markdown(report), encoding="utf-8")
    return path


def format_candidate_evidence_triage_markdown(report: dict[str, Any], workspace_root: str | Path = ".") -> str:
    """Format a compact, human-facing triage report with source titles."""

    resolver = SourceTitleResolver(workspace_root)
    lines = [
        "# Candidate Evidence Triage",
        "",
        "This is the human review surface for candidate evidence questions.",
        "",
        "## How To Read This File",
        "",
        "- Rank means retrieval order, not mathematical importance.",
        "- Rank 1 is the system's strongest current match.",
        "- Review only ranks 1-3 first.",
        "- Fill `Best evidence rank:` with ranks such as `1`, `1,2`, `3`, `drop`, or `fix: <short note>`.",
        "- Leave `Best evidence rank:` blank when the question looks fine and rank 1 is the best evidence.",
        "",
        f"Candidate questions: {report['total_questions']}",
        f"Negative questions: {report['negative_questions']}",
        f"Top-k retrieved: {report['top_k']}",
        "",
    ]

    for row in report["rows"]:
        lines.extend(
            [
                f"## {row['id']}",
                "",
                f"Question: {row['question']}",
            ]
        )
        if row["negative"]:
            lines.extend(["", "Negative: true"])

        lines.extend(["", "Expected:"])
        if row["expected_sources"]:
            for source in row["expected_sources"]:
                lines.append(f"- {source} - {resolver.title_for_reference(source)}")
        else:
            lines.append("- none")

        lines.extend(["", "Top evidence:"])
        for chunk_row in row["top_chunks"][:3]:
            source_id = resolver.display_id_for_path(chunk_row["source_path"])
            title = resolver.title_for_path(chunk_row["source_path"])
            location = f" - {chunk_row['location']}" if chunk_row["location"] else ""
            section = chunk_row["section_path"] if chunk_row["section_path"] else "unsectioned"
            lines.extend(
                [
                    (
                        f"{chunk_row['rank']}. {source_id} - {title}"
                    ),
                    f"   {section}{location}",
                    f"   {chunk_row['snippet']}",
                    "",
                ]
            )
        if not row["top_chunks"]:
            lines.extend(["- none", ""])

        lines.extend(
            [
                "Best evidence rank:",
                "",
            ]
        )
    return "\n".join(lines).rstrip() + "\n"


def write_candidate_evidence_triage_markdown(
    report: dict[str, Any],
    out_path: str | Path,
    workspace_root: str | Path = ".",
) -> Path:
    path = Path(out_path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(format_candidate_evidence_triage_markdown(report, workspace_root), encoding="utf-8")
    return path


class SourceTitleResolver:
    def __init__(self, workspace_root: str | Path = "."):
        self.workspace_root = Path(workspace_root)
        self._metadata_cache: dict[str, dict[str, Any]] = {}

    def title_for_reference(self, reference: str) -> str:
        note_title = self._friendly_note_title(reference)
        if note_title:
            return note_title
        arxiv_id = self._arxiv_id_from_reference(reference)
        if arxiv_id:
            title = self._arxiv_title(arxiv_id)
            if title:
                return title
        return reference

    def title_for_path(self, source_path: str) -> str:
        note_title = self._friendly_note_title(source_path)
        if note_title:
            return note_title
        arxiv_id = self._arxiv_id_from_path(source_path)
        if arxiv_id:
            title = self._arxiv_title(arxiv_id)
            if title:
                return title
        return source_path

    def display_id_for_path(self, source_path: str) -> str:
        arxiv_id = self._arxiv_id_from_path(source_path)
        if arxiv_id:
            return arxiv_id
        return Path(source_path).name or source_path

    def _arxiv_title(self, arxiv_dirname: str) -> str | None:
        metadata = self._arxiv_metadata(arxiv_dirname)
        title = metadata.get("title")
        return normalize_whitespace(str(title)) if title else None

    def _arxiv_metadata(self, arxiv_dirname: str) -> dict[str, Any]:
        safe_dirname = arxiv_dirname.replace("/", "_")
        if safe_dirname not in self._metadata_cache:
            metadata_path = self.workspace_root / "corpus" / "arxiv" / safe_dirname / "metadata.yaml"
            self._metadata_cache[safe_dirname] = _read_yaml_mapping(metadata_path)
        return self._metadata_cache[safe_dirname]

    @staticmethod
    def _arxiv_id_from_path(source_path: str) -> str | None:
        parts = source_path.replace("\\", "/").split("/")
        try:
            index = parts.index("arxiv")
        except ValueError:
            return None
        if index + 1 >= len(parts):
            return None
        return parts[index + 1]

    @staticmethod
    def _arxiv_id_from_reference(reference: str) -> str | None:
        path_id = SourceTitleResolver._arxiv_id_from_path(reference)
        if path_id:
            return path_id
        value = reference.strip().replace("\\", "/")
        if not value or value.startswith("corpus/my_notes/"):
            return None
        return value.replace("/", "_")

    @staticmethod
    def _friendly_note_title(value: str) -> str | None:
        normalized = value.replace("\\", "/")
        if "corpus/my_notes/" not in normalized:
            return None
        return FRIENDLY_NOTE_TITLES.get(Path(normalized).name)


def _result_to_inspection_row(result: SearchResult, question: CandidateEvidenceQuestion) -> dict[str, Any]:
    chunk = result.chunk
    matched_terms = _matched_expected_terms(chunk.content, question.expected_terms)
    return {
        "rank": result.rank,
        "score": result.score,
        "source_path": chunk.source_path,
        "chunk_type": chunk.chunk_type,
        "section_path": format_section_path(chunk),
        "location": _line_or_page_location(chunk),
        "snippet": make_snippet(chunk.content, question.question),
        "source_matches_expected": any(
            _chunk_matches_expected_source(chunk, expected) for expected in question.expected_sources
        ),
        "chunk_type_matches_expected": chunk.chunk_type in set(question.expected_chunk_types),
        "matched_expected_terms": matched_terms,
    }


def _matched_expected_terms(content: str, expected_terms: list[str]) -> list[str]:
    normalized_content = normalize_whitespace(content).casefold()
    return [term for term in expected_terms if normalize_whitespace(term).casefold() in normalized_content]


def _line_or_page_location(chunk) -> str:
    parts: list[str] = []
    if chunk.page_number is not None:
        parts.append(f"p. {chunk.page_number}")
    if chunk.line_start is not None and chunk.line_end is not None:
        if chunk.line_start == chunk.line_end:
            parts.append(f"line {chunk.line_start}")
        else:
            parts.append(f"lines {chunk.line_start}-{chunk.line_end}")
    elif chunk.line_start is not None:
        parts.append(f"line {chunk.line_start}")
    return ", ".join(parts)


def _required_string(item: dict[str, Any], field_name: str, index: int) -> str:
    value = item.get(field_name)
    if not isinstance(value, str) or not value.strip():
        raise ValueError(f"Candidate question entry {index} is missing a non-empty {field_name}.")
    return value.strip()


def _string_list(item: dict[str, Any], field_name: str, question_id: str) -> list[str]:
    value = item.get(field_name)
    if value is None:
        return []
    if not isinstance(value, list) or not all(isinstance(entry, str) for entry in value):
        raise ValueError(f"Candidate question {question_id} {field_name} must be a list of strings.")
    return [entry.strip() for entry in value if entry.strip()]


def _rubric(value: Any, question_id: str) -> dict[str, str]:
    if not isinstance(value, dict):
        raise ValueError(f"Candidate question {question_id} relevance_rubric must be a mapping.")
    return {str(key): str(entry) for key, entry in value.items()}


def _review_status(value: Any, question_id: str) -> str:
    if not isinstance(value, str) or not value.strip():
        raise ValueError(f"Candidate question {question_id} review_status must be a non-empty string.")
    status = value.strip()
    if status not in VALID_REVIEW_STATUSES:
        allowed = ", ".join(sorted(VALID_REVIEW_STATUSES))
        raise ValueError(f"Candidate question {question_id} has invalid review_status {status!r}; expected one of: {allowed}.")
    return status


def _optional_string(item: dict[str, Any], field_name: str, question_id: str) -> str:
    value = item.get(field_name)
    if not isinstance(value, str):
        raise ValueError(f"Candidate question {question_id} {field_name} must be a string.")
    return value


def _read_yaml_mapping(path: Path) -> dict[str, Any]:
    if not path.exists():
        return {}
    try:
        import yaml  # type: ignore

        data = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    except Exception:
        return {}
    return data if isinstance(data, dict) else {}


def _count_true(rows: list[dict[str, Any]], key: str) -> int:
    return sum(1 for row in rows if row["diagnostics"][key])


def _format_list(values: list[str]) -> str:
    return ", ".join(f"`{value}`" for value in values) if values else "-"


def _yes_no(value: bool) -> str:
    return "yes" if value else "no"


def _escape_pipes(value: str) -> str:
    return normalize_whitespace(value).replace("|", "\\|")
