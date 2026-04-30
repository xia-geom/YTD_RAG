"""Candidate paper discovery workflow."""

from __future__ import annotations

from collections import Counter
from dataclasses import dataclass

from .arxiv_client import ArxivClient, ArxivPaper, build_arxiv_query
from .index_store import IndexStore
from .paper_ranker import DiscoveryConfig, discovery_query_phrases, load_discovery_config, rank_papers
from .paper_store import DEFAULT_CANDIDATES_PATH, PaperCandidate, write_candidates
from .text_cleaning import salient_terms


@dataclass
class DiscoveryResult:
    candidates: list[PaperCandidate]
    low_confidence_candidates: list[PaperCandidate]
    warnings: list[str]
    arxiv_query: str


def discover_candidates(
    query: str | None = None,
    config_path: str | None = None,
    output_path: str = DEFAULT_CANDIDATES_PATH,
    index_dir: str = ".math_rag_index",
    max_results: int | None = None,
    sort_by: str = "relevance",
    client: ArxivClient | None = None,
) -> DiscoveryResult:
    config = load_discovery_config(config_path)
    limit = max_results or config.download_policy.max_papers_per_run
    discovery_query = query or " ".join(config.seed_keywords[:6])
    phrases = discovery_query_phrases(discovery_query, config)
    arxiv_query = build_arxiv_query(
        query=None,
        authors=None if query else config.seed_authors[:8],
        categories=config.arxiv_categories,
        phrases=phrases[:8],
    )
    client = client or ArxivClient(delay_seconds=config.download_policy.delay_seconds_between_requests)
    warnings: list[str] = []
    try:
        papers = client.search(arxiv_query, max_results=limit, sort_by=sort_by)
    except Exception as exc:
        warnings.append(f"arXiv discovery failed: {exc}")
        papers = []

    candidates = rank_papers(
        _dedupe_papers(papers),
        config,
        query=discovery_query,
        existing_corpus_terms=extract_existing_corpus_terms(index_dir),
    )
    candidates = candidates[:limit]
    if config.exclude_low_confidence_by_default:
        main_candidates = [candidate for candidate in candidates if candidate.confidence != "low"]
        low_confidence = [candidate for candidate in candidates if candidate.confidence == "low"]
    else:
        main_candidates = candidates
        low_confidence = []
    write_candidates(output_path, main_candidates, low_confidence)
    return DiscoveryResult(main_candidates, low_confidence, warnings, arxiv_query)


def extract_existing_corpus_terms(index_dir: str, limit: int = 40) -> set[str]:
    chunks = IndexStore(index_dir).load_chunks()
    counter: Counter[str] = Counter()
    for chunk in chunks:
        counter.update(term for term in salient_terms(chunk.content) if len(term) >= 5)
        counter.update(chunk.topics)
    return {term for term, _ in counter.most_common(limit)}


def _dedupe_papers(papers: list[ArxivPaper]) -> list[ArxivPaper]:
    seen: set[tuple[str, str | None]] = set()
    result: list[ArxivPaper] = []
    for paper in papers:
        key = (paper.arxiv_id, paper.version)
        if key in seen:
            continue
        seen.add(key)
        result.append(paper)
    return result
