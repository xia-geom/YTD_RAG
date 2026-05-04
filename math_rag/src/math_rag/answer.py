"""Retrieval-grounded answer template.

This module deliberately does not try to prove or verify mathematics. It builds
a structured report from retrieved chunks and marks anything beyond direct
evidence as an inference requiring human verification.
"""

from __future__ import annotations

from .citations import format_citation, format_location, unique_sources
from .models import SearchResult
from .symbol_normalization import normalize_search_text
from .text_cleaning import make_snippet, salient_terms


LOW_CONFIDENCE_THRESHOLD = 0.05
DOMAIN_SPECIFIC_TERMS = {
    "abreu",
    "berman-darvas-lu",
    "chen-cheng",
    "cone",
    "conic",
    "cscK".lower(),
    "cusp",
    "ding",
    "donaldson",
    "extremal",
    "geodesics",
    "kahler",
    "kähler",
    "lahdili",
    "mabuchi",
    "monge-ampere",
    "monge-ampère",
    "poincare",
    "poincaré",
    "polytope",
    "toric",
    "twisted",
    "weighted",
    "yau-tian-donaldson",
}


def retrieval_confidence(question: str, results: list[SearchResult]) -> str:
    if not results:
        return "low"
    if max(result.score for result in results) < LOW_CONFIDENCE_THRESHOLD:
        return "low"
    query_terms = salient_terms(question)
    if not query_terms:
        return "low"
    for result in results[:3]:
        matched = _matched_terms(question, result)
        if len(matched) >= 2:
            return "usable"
        if matched and _is_specific_term(matched[0]) and (result.keyword_score > 0 or result.score >= 0.2):
            return "usable"
    return "low"


def build_answer(question: str, results: list[SearchResult], top_evidence: int = 5) -> str:
    confidence = retrieval_confidence(question, results)
    lines: list[str] = [f"Question:\n{question}", ""]

    if confidence == "low":
        lines.extend(
            [
                "Short answer:",
                "I do not find enough evidence in the retrieved corpus to answer this reliably. This is a retrieval failure, not a mathematical conclusion.",
                "",
                "Retrieved evidence:",
            ]
        )
        if results:
            lines.extend(_evidence_lines(question, results[:top_evidence]))
        else:
            lines.append("No chunks were retrieved.")
        lines.extend(
            [
                "",
                "What the corpus supports:",
                "- Nothing specific is established by the retrieved passages.",
                "",
                "Reasonable inference:",
                "- No reliable inference should be drawn from this retrieval result.",
                "",
                "Not established by retrieved sources:",
                "- The corpus search did not establish the requested statement, proof, comparison, or novelty claim.",
                "- This requires human verification and likely broader search terms or more documents.",
                "",
                "Possible relevance to my research:",
                "- Try exact names, theorem labels, formulas, author names, or related terms from your notes.",
                "",
                "Sources inspected:",
            ]
        )
        lines.extend(_sources_lines(results))
        return "\n".join(lines)

    top_results = results[:top_evidence]
    lines.extend(
        [
            "Short answer:",
            "The corpus contains retrieved passages that appear relevant to the question. The report below is based only on those passages and does not verify any proof or theorem.",
            "",
            "Retrieved evidence:",
        ]
    )
    lines.extend(_evidence_lines(question, top_results))

    lines.extend(["", "What the corpus supports:"])
    for result in top_results:
        terms = _matched_terms(question, result)
        if terms:
            lines.append(
                f"- The source contains retrieved text overlapping the query terms {', '.join(terms[:6])} {format_citation(result.chunk)}."
            )
        else:
            lines.append(f"- The source was retrieved as relevant by the local index {format_citation(result.chunk)}.")

    lines.extend(["", "Reasonable inference:"])
    if top_results:
        best = top_results[0]
        lines.append(
            f"- A cautious next step is to inspect {best.chunk.source_path} around {format_location(best.chunk)}; it is the strongest retrieved match, not a verified mathematical conclusion {format_citation(best.chunk)}."
        )
    else:
        lines.append("- No reliable inference should be drawn.")

    lines.extend(
        [
            "",
            "Not established by retrieved sources:",
            "- The retrieved passages do not establish correctness of any proof.",
            "- They do not establish novelty, completeness of hypotheses, or equivalence of theorem statements unless those points are explicitly present in the cited text.",
            "- This requires human verification in the surrounding source context.",
            "",
            "Possible relevance to my research:",
            "- Use the cited chunks as entry points for literature review, theorem comparison, citation recovery, or locating forgotten notes.",
            "",
            "Sources inspected:",
        ]
    )
    lines.extend(_sources_lines(results))
    return "\n".join(lines)


def _evidence_lines(question: str, results: list[SearchResult]) -> list[str]:
    lines: list[str] = []
    for index, result in enumerate(results, start=1):
        chunk = result.chunk
        lines.extend(
            [
                f"{index}. {format_location(chunk)}",
                f"   Chunk type: {chunk.chunk_type}; score: {result.score:.3f}",
                "   Relevant excerpt:",
                f"   {make_snippet(chunk.content, question)}",
                "",
            ]
        )
    if lines and lines[-1] == "":
        lines.pop()
    return lines


def _matched_terms(question: str, result: SearchResult) -> list[str]:
    content = normalize_search_text(result.chunk.content)
    return [term for term in salient_terms(question) if normalize_search_text(term) in content]


def _is_specific_term(term: str) -> bool:
    lowered = term.lower()
    return (
        lowered in DOMAIN_SPECIFIC_TERMS
        or len(lowered) >= 7
        or "-" in lowered
        or "\\" in lowered
        or any(char.isdigit() for char in lowered)
    )


def _sources_lines(results: list[SearchResult]) -> list[str]:
    sources = unique_sources(results)
    if not sources:
        return ["- No sources inspected."]
    return [f"- {source}" for source in sources]
