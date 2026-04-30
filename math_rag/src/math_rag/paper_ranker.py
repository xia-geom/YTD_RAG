"""Ranking of candidate papers for math_rag discovery."""

from __future__ import annotations

import re
import unicodedata
from dataclasses import dataclass, field
from datetime import datetime
from typing import Any

from .arxiv_client import ArxivPaper
from .paper_store import PaperCandidate, load_yaml_file


PROTECTED_PHRASES = [
    "constant scalar curvature Kähler",
    "constant scalar curvature Kahler",
    "cscK",
    "extremal Kähler",
    "extremal Kahler",
    "toric Kähler",
    "toric Kahler",
    "Abreu equation",
    "Mabuchi energy",
    "Mabuchi",
    "K-energy",
    "Ding functional",
    "weak geodesic",
    "finite energy",
    "conic Kähler",
    "conic Kahler",
    "cone angle",
    "Poincaré metric",
    "Poincare metric",
    "Poincaré type",
    "Poincare type",
    "cusp metric",
    "K-stability",
    "Yau-Tian-Donaldson",
    "weighted extremal",
    "twisted K-energy",
]
PROTECTED_PHRASE_NORMS = {unicodedata.normalize("NFKD", phrase).encode("ascii", "ignore").decode("ascii").lower() for phrase in PROTECTED_PHRASES}

WEAK_TOKENS = {
    "constant",
    "scalar",
    "curvature",
    "equation",
    "metric",
    "metrics",
    "geometry",
    "kahler",
    "kähler",
    "toric",
    "variety",
    "varieties",
    "energy",
}

DOMAIN_EXACT_TERMS = {
    "csck",
    "mabuchi",
    "k-energy",
    "abreu equation",
    "conic kahler",
    "conic kähler",
    "weak geodesic",
    "finite energy",
    "k-stability",
}

TOKEN_RE = re.compile(r"[A-Za-zÀ-ÖØ-öø-ÿ]+(?:-[A-Za-zÀ-ÖØ-öø-ÿ]+)*")


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
    weak_token_bonus: float = 0.2


@dataclass
class DownloadPolicy:
    require_approval: bool = True
    max_papers_per_run: int = 20
    delay_seconds_between_requests: float = 4.0
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
    exclude_low_confidence_by_default: bool = True


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
        exclude_low_confidence_by_default=bool(data.get("exclude_low_confidence_by_default", True)),
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
    title_norm = normalize_math_text(paper.title)
    abstract_norm = normalize_math_text(paper.abstract)
    all_text_norm = f"{title_norm} {abstract_norm}"
    query_terms = parse_discovery_query(query)
    phrase_pool = _dedupe_phrases([*PROTECTED_PHRASES, *config.seed_keywords, *query_terms.protected_phrases])
    protected_match_count = 0

    for phrase in phrase_pool:
        phrase_norm = normalize_math_text(phrase)
        if not phrase_norm or (_is_weak_only_phrase(phrase_norm) and phrase_norm not in PROTECTED_PHRASE_NORMS):
            continue
        if _contains_phrase(title_norm, phrase_norm):
            protected_match_count += 1
            score += weights.keyword_match + weights.title_match
            reasons.append(f"strong title phrase match: {canonical_phrase(phrase)}")
        elif _contains_phrase(abstract_norm, phrase_norm):
            protected_match_count += 1
            score += weights.keyword_match + weights.abstract_match
            reasons.append(f"strong abstract phrase match: {canonical_phrase(phrase)}")

    seed_author_match = False
    for seed_author in config.seed_authors:
        if any(seed_author.lower() in author.lower() for author in paper.authors):
            seed_author_match = True
            score += weights.author_match
            reasons.append(f"seed author match: {seed_author}")

    whitelist_match = _matches_manual_list(paper, config.manual_whitelist)
    blacklist_match = _matches_manual_list(paper, config.manual_blacklist)
    has_domain_anchor = protected_match_count > 0 or seed_author_match or whitelist_match

    weak_matches = [token for token in query_terms.weak_tokens if _contains_token(all_text_norm, normalize_math_text(token))]
    if weak_matches:
        if has_domain_anchor:
            bonus = min(len(weak_matches), 4) * weights.weak_token_bonus
            score += bonus
            for token in weak_matches[:4]:
                reasons.append(f"weak token bonus: {token}")
        else:
            for token in weak_matches[:4]:
                reasons.append(f"weak token match only: {token}")
            reasons.append("demoted: no protected phrase or seed author match")

    for category in paper.categories:
        if category in config.arxiv_categories:
            score += weights.category_match
            reasons.append(f"category match: {category}")

    if paper.year:
        current_year = datetime.now().year
        if paper.year >= current_year - 5:
            score += weights.recency
            reasons.append(f"recent paper: {paper.year}")

    for term in sorted(existing_corpus_terms or set()):
        term_norm = normalize_math_text(term)
        if term_norm and not _is_weak_only_phrase(term_norm) and _contains_phrase(all_text_norm, term_norm):
            score += weights.corpus_keyword_match
            reasons.append(f"existing corpus phrase match: {term}")

    if whitelist_match:
        score += weights.whitelist_bonus
        reasons.append("manual whitelist bonus")

    if blacklist_match:
        score += weights.blacklist_penalty
        reasons.append("manual blacklist penalty")

    normalized = max(-1.0, min(1.0, score / 10.0))
    confidence = classify_confidence(normalized, protected_match_count, seed_author_match, whitelist_match, blacklist_match)
    return PaperCandidate(
        arxiv_id=paper.arxiv_id,
        version=paper.version,
        title=paper.title,
        authors=paper.authors,
        year=paper.year,
        arxiv_categories=paper.categories,
        abstract=paper.abstract,
        score=normalized,
        confidence=confidence,
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


@dataclass(frozen=True)
class ParsedDiscoveryQuery:
    protected_phrases: list[str]
    weak_tokens: list[str]
    other_terms: list[str]


def parse_discovery_query(query: str | None) -> ParsedDiscoveryQuery:
    if not query:
        return ParsedDiscoveryQuery([], [], [])
    normalized = normalize_math_text(query)
    protected: list[str] = []
    remainder = f" {normalized} "
    for phrase in sorted(PROTECTED_PHRASES, key=len, reverse=True):
        phrase_norm = normalize_math_text(phrase)
        if _contains_phrase(normalized, phrase_norm):
            protected.append(canonical_phrase(phrase))
            remainder = re.sub(rf"(?<!\w){re.escape(phrase_norm)}(?!\w)", " ", remainder)
    tokens = _dedupe(TOKEN_RE.findall(remainder))
    weak = [token for token in tokens if normalize_math_text(token) in WEAK_TOKENS]
    other = [token for token in tokens if normalize_math_text(token) not in WEAK_TOKENS]
    return ParsedDiscoveryQuery(_dedupe(protected), weak, other)


def discovery_query_phrases(query: str | None, config: DiscoveryConfig) -> list[str]:
    parsed = parse_discovery_query(query)
    if parsed.protected_phrases:
        phrases = list(parsed.protected_phrases)
        phrase_norms = {normalize_math_text(phrase) for phrase in phrases}
        weak_norms = {normalize_math_text(token) for token in parsed.weak_tokens}
        if "constant scalar curvature kahler" in phrase_norms:
            phrases.append("cscK")
        if "toric" in weak_norms and ("constant scalar curvature kahler" in phrase_norms or "csck" in phrase_norms):
            phrases.extend(["toric Kähler", "toric cscK"])
        return _dedupe(phrases)
    return [
        phrase
        for phrase in config.seed_keywords
        if normalize_math_text(phrase) in PROTECTED_PHRASE_NORMS or not _is_weak_only_phrase(normalize_math_text(phrase))
    ]


def classify_confidence(
    score: float,
    protected_match_count: int,
    seed_author_match: bool,
    whitelist_match: bool,
    blacklist_match: bool,
) -> str:
    if blacklist_match:
        return "low"
    if whitelist_match or seed_author_match or protected_match_count >= 2:
        return "high"
    if protected_match_count >= 1 or seed_author_match:
        return "medium" if score < 0.55 else "high"
    return "low"


def config_to_dict(config: DiscoveryConfig) -> dict[str, Any]:
    return {
        "seed_authors": config.seed_authors,
        "seed_keywords": config.seed_keywords,
        "arxiv_categories": config.arxiv_categories,
        "ranking_weights": config.ranking_weights.__dict__,
        "download_policy": config.download_policy.__dict__,
        "manual_whitelist": config.manual_whitelist,
        "manual_blacklist": config.manual_blacklist,
        "exclude_low_confidence_by_default": config.exclude_low_confidence_by_default,
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


def _dedupe_phrases(values: list[str]) -> list[str]:
    seen: set[str] = set()
    result: list[str] = []
    for value in values:
        key = normalize_math_text(value)
        if key and key not in seen:
            seen.add(key)
            result.append(canonical_phrase(value))
    return result


def normalize_math_text(text: str) -> str:
    normalized = unicodedata.normalize("NFKD", text)
    ascii_text = "".join(char for char in normalized if not unicodedata.combining(char))
    return re.sub(r"\s+", " ", ascii_text.lower().replace("kähler", "kahler")).strip()


def canonical_phrase(phrase: str) -> str:
    phrase_norm = normalize_math_text(phrase)
    for protected in PROTECTED_PHRASES:
        if normalize_math_text(protected) == phrase_norm:
            return protected
    return phrase


def _contains_phrase(text_norm: str, phrase_norm: str) -> bool:
    return re.search(rf"(?<!\w){re.escape(phrase_norm)}(?!\w)", text_norm) is not None


def _contains_token(text_norm: str, token_norm: str) -> bool:
    return re.search(rf"(?<!\w){re.escape(token_norm)}(?!\w)", text_norm) is not None


def _is_weak_only_phrase(phrase_norm: str) -> bool:
    tokens = TOKEN_RE.findall(phrase_norm)
    return bool(tokens) and all(token in WEAK_TOKENS for token in tokens)
