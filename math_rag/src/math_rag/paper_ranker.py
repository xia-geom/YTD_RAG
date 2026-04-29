"""Ranking of candidate papers for math_rag discovery."""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from typing import Any

from .arxiv_client import ArxivPaper
from .paper_store import PaperCandidate, load_yaml_file
from .text_cleaning import salient_terms


DEFAULT_SEED_AUTHORS = [
    "Berman",
    "Darvas",
    "Lu",
    "Chen",
    "Cheng",
    "Lahdili",
    "Apostolov",
    "Auvray",
    "Sektnan",
    "Donaldson",
    "Székelyhidi",
    "Tian",
    "Boucksom",
    "Jonsson",
    "Guedj",
    "Zeriahi",
    "Berndtsson",
]

DEFAULT_SEED_KEYWORDS = [
    "constant scalar curvature Kähler",
    "cscK",
    "Mabuchi energy",
    "K-energy",
    "Ding functional",
    "toric Kähler",
    "toric variety",
    "moment polytope",
    "Abreu equation",
    "extremal Kähler metric",
    "conic Kähler metric",
    "cone angle",
    "Poincare metric",
    "Poincaré metric",
    "cusp metric",
    "log K-energy",
    "twisted K-energy",
    "weighted extremal metric",
    "weak geodesic",
    "finite energy",
    "Yau-Tian-Donaldson",
    "K-stability",
]

DEFAULT_ARXIV_CATEGORIES = ["math.DG", "math.AG", "math.CV"]


@dataclass
class RankingWeights:
    keyword_match: float = 3.0
    author_match: float = 2.5
    title_match: float = 2.0
    abstract_match: float = 1.5
    category_match: float = 1.0
    recency: float = 0.5
    corpus_keyword_match: float = 0.8
    blacklist_penalty: float = -10.0
    whitelist_bonus: float = 5.0


@dataclass
class DownloadPolicy:
    require_approval: bool = True
    max_papers_per_run: int = 20
    delay_seconds_between_requests: float = 3.0
    download_source: bool = True
    download_pdf: bool = True
    avoid_duplicates: bool = True


@dataclass
class DiscoveryConfig:
    seed_authors: list[str] = field(default_factory=lambda: list(DEFAULT_SEED_AUTHORS))
    seed_keywords: list[str] = field(default_factory=lambda: list(DEFAULT_SEED_KEYWORDS))
    arxiv_categories: list[str] = field(default_factory=lambda: list(DEFAULT_ARXIV_CATEGORIES))
    ranking_weights: RankingWeights = field(default_factory=RankingWeights)
    download_policy: DownloadPolicy = field(default_factory=DownloadPolicy)
    manual_whitelist: list[str] = field(default_factory=list)
    manual_blacklist: list[str] = field(default_factory=list)


def load_discovery_config(path: str | None = None) -> DiscoveryConfig:
    if not path:
        return DiscoveryConfig()
    data = load_yaml_file(path)
    if not data:
        return DiscoveryConfig()
    weights = RankingWeights(**{**RankingWeights().__dict__, **(data.get("ranking_weights") or {})})
    policy = DownloadPolicy(**{**DownloadPolicy().__dict__, **(data.get("download_policy") or {})})
    return DiscoveryConfig(
        seed_authors=list(data.get("seed_authors") or DEFAULT_SEED_AUTHORS),
        seed_keywords=list(data.get("seed_keywords") or DEFAULT_SEED_KEYWORDS),
        arxiv_categories=list(data.get("arxiv_categories") or DEFAULT_ARXIV_CATEGORIES),
        ranking_weights=weights,
        download_policy=policy,
        manual_whitelist=list(data.get("manual_whitelist") or []),
        manual_blacklist=list(data.get("manual_blacklist") or []),
    )


def rank_paper(
    paper: ArxivPaper,
    config: DiscoveryConfig,
    query: str | None = None,
    existing_corpus_terms: set[str] | None = None,
) -> PaperCandidate:
    weights = config.ranking_weights
    score = 0.0
    reasons: list[str] = []
    title_lower = paper.title.lower()
    abstract_lower = paper.abstract.lower()
    all_text = f"{paper.title} {paper.abstract}".lower()

    keyword_pool = list(config.seed_keywords)
    if query:
        keyword_pool.extend(salient_terms(query))

    for keyword in _dedupe(keyword_pool):
        keyword_lower = keyword.lower()
        if not keyword_lower:
            continue
        if keyword_lower in all_text:
            score += weights.keyword_match
            reasons.append(f"matched keyword: {keyword}")
        if keyword_lower in title_lower:
            score += weights.title_match
            reasons.append(f"title matched keyword: {keyword}")
        elif keyword_lower in abstract_lower:
            score += weights.abstract_match
            reasons.append(f"abstract matched keyword: {keyword}")

    for seed_author in config.seed_authors:
        if any(seed_author.lower() in author.lower() for author in paper.authors):
            score += weights.author_match
            reasons.append(f"matched seed author: {seed_author}")

    for category in paper.categories:
        if category in config.arxiv_categories:
            score += weights.category_match
            reasons.append(f"category {category} is in configured categories")

    if paper.year:
        current_year = datetime.now().year
        if paper.year >= current_year - 5:
            score += weights.recency
            reasons.append(f"recent paper: {paper.year}")

    for term in sorted(existing_corpus_terms or set()):
        if term and term.lower() in all_text:
            score += weights.corpus_keyword_match
            reasons.append(f"matched existing corpus term: {term}")

    if _matches_manual_list(paper, config.manual_whitelist):
        score += weights.whitelist_bonus
        reasons.append("manual whitelist bonus")

    if _matches_manual_list(paper, config.manual_blacklist):
        score += weights.blacklist_penalty
        reasons.append("manual blacklist penalty")

    normalized = max(-1.0, min(1.0, score / 20.0))
    return PaperCandidate(
        arxiv_id=paper.arxiv_id,
        version=paper.version,
        title=paper.title,
        authors=paper.authors,
        year=paper.year,
        arxiv_categories=paper.categories,
        abstract=paper.abstract,
        score=normalized,
        ranking_reasons=_dedupe(reasons),
        status="pending",
        action="pending",
        source_url=paper.source_url,
        pdf_url=paper.pdf_url,
    )


def rank_papers(
    papers: list[ArxivPaper],
    config: DiscoveryConfig,
    query: str | None = None,
    existing_corpus_terms: set[str] | None = None,
) -> list[PaperCandidate]:
    candidates = [rank_paper(paper, config, query=query, existing_corpus_terms=existing_corpus_terms) for paper in papers]
    candidates.sort(key=lambda candidate: (candidate.score, candidate.year or 0, candidate.title), reverse=True)
    return candidates


def config_to_dict(config: DiscoveryConfig) -> dict[str, Any]:
    return {
        "seed_authors": config.seed_authors,
        "seed_keywords": config.seed_keywords,
        "arxiv_categories": config.arxiv_categories,
        "ranking_weights": config.ranking_weights.__dict__,
        "download_policy": config.download_policy.__dict__,
        "manual_whitelist": config.manual_whitelist,
        "manual_blacklist": config.manual_blacklist,
    }


def _matches_manual_list(paper: ArxivPaper, values: list[str]) -> bool:
    haystack = " ".join([paper.arxiv_id, paper.title, *paper.authors]).lower()
    return any(value.lower() in haystack for value in values)


def _dedupe(values: list[str]) -> list[str]:
    seen: set[str] = set()
    result: list[str] = []
    for value in values:
        if value not in seen:
            seen.add(value)
            result.append(value)
    return result
