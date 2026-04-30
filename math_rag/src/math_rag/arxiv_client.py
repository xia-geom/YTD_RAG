"""Small arXiv API client using the official Atom metadata endpoint."""

from __future__ import annotations

import time
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from dataclasses import dataclass, field
from datetime import datetime


ARXIV_API_URL = "https://export.arxiv.org/api/query"
ARXIV_ABS_URL = "https://arxiv.org/abs"
ARXIV_PDF_URL = "https://arxiv.org/pdf"
ARXIV_SOURCE_URL = "https://arxiv.org/e-print"
ATOM_NS = {"atom": "http://www.w3.org/2005/Atom", "arxiv": "http://arxiv.org/schemas/atom"}


@dataclass
class ArxivPaper:
    arxiv_id: str
    version: str | None
    title: str
    authors: list[str]
    abstract: str
    year: int | None
    categories: list[str] = field(default_factory=list)
    published: str | None = None
    updated: str | None = None
    source_url: str | None = None
    pdf_url: str | None = None


class ArxivClient:
    def __init__(self, delay_seconds: float = 3.0, user_agent: str = "math_rag/0.1 local research tool"):
        self.delay_seconds = delay_seconds
        self.user_agent = user_agent
        self._last_request_at = 0.0

    def search(self, query: str, max_results: int = 20, start: int = 0, sort_by: str = "relevance") -> list[ArxivPaper]:
        params = {
            "search_query": query,
            "start": str(start),
            "max_results": str(max_results),
            "sortBy": _normalize_sort_by(sort_by),
            "sortOrder": "descending",
        }
        url = f"{ARXIV_API_URL}?{urllib.parse.urlencode(params)}"
        text = self.get_text(url)
        return parse_arxiv_atom(text)

    def get_text(self, url: str) -> str:
        return self.download_bytes(url).decode("utf-8", errors="replace")

    def download_bytes(self, url: str) -> bytes:
        self._respect_delay()
        request = urllib.request.Request(url, headers={"User-Agent": self.user_agent})
        with urllib.request.urlopen(request, timeout=60) as response:
            return response.read()

    def _respect_delay(self) -> None:
        elapsed = time.monotonic() - self._last_request_at
        if self._last_request_at and elapsed < self.delay_seconds:
            time.sleep(self.delay_seconds - elapsed)
        self._last_request_at = time.monotonic()


def parse_arxiv_atom(xml_text: str) -> list[ArxivPaper]:
    root = ET.fromstring(xml_text)
    papers: list[ArxivPaper] = []
    for entry in root.findall("atom:entry", ATOM_NS):
        raw_id = _text(entry, "atom:id") or ""
        arxiv_id, version = split_arxiv_id(raw_id.rsplit("/", 1)[-1])
        title = _normalize(_text(entry, "atom:title") or "")
        abstract = _normalize(_text(entry, "atom:summary") or "")
        authors = [
            _normalize(name.text or "")
            for name in entry.findall("atom:author/atom:name", ATOM_NS)
            if _normalize(name.text or "")
        ]
        published = _text(entry, "atom:published")
        updated = _text(entry, "atom:updated")
        year = _year_from_date(published or updated)
        categories = [
            category.attrib.get("term", "")
            for category in entry.findall("atom:category", ATOM_NS)
            if category.attrib.get("term")
        ]
        pdf_url = None
        for link in entry.findall("atom:link", ATOM_NS):
            if link.attrib.get("title") == "pdf" or link.attrib.get("type") == "application/pdf":
                pdf_url = link.attrib.get("href")
                break
        id_with_version = f"{arxiv_id}{version or ''}"
        papers.append(
            ArxivPaper(
                arxiv_id=arxiv_id,
                version=version,
                title=title,
                authors=authors,
                abstract=abstract,
                year=year,
                categories=categories,
                published=published,
                updated=updated,
                source_url=f"{ARXIV_SOURCE_URL}/{id_with_version}",
                pdf_url=pdf_url or f"{ARXIV_PDF_URL}/{id_with_version}",
            )
        )
    return papers


def split_arxiv_id(identifier: str) -> tuple[str, str | None]:
    identifier = identifier.strip()
    if "arxiv:" in identifier.lower():
        identifier = identifier.split(":", 1)[1]
    if "v" in identifier and identifier.rsplit("v", 1)[-1].isdigit():
        base, version_num = identifier.rsplit("v", 1)
        return base, f"v{version_num}"
    return identifier, None


def build_arxiv_query(
    query: str | None = None,
    authors: list[str] | None = None,
    categories: list[str] | None = None,
    phrases: list[str] | None = None,
) -> str:
    term_parts: list[str] = []
    for phrase in phrases or []:
        escaped = _escape_query_term(phrase)
        term_parts.append(f'ti:"{escaped}"')
        term_parts.append(f'abs:"{escaped}"')
        term_parts.append(f'all:"{escaped}"')
    if query:
        terms = [term for term in query.replace(",", " ").split() if term]
        term_parts.extend(f'all:"{_escape_query_term(term)}"' for term in terms[:4])
    author_parts: list[str] = []
    for author in authors or []:
        author_parts.append(f'au:"{_escape_query_term(author)}"')
    category_parts: list[str] = []
    for category in categories or []:
        category_parts.append(f"cat:{category}")

    main_clauses = []
    if term_parts:
        main_clauses.append("(" + " OR ".join(term_parts) + ")")
    if author_parts:
        main_clauses.append("(" + " OR ".join(author_parts) + ")")
    main = " OR ".join(main_clauses)
    category = "(" + " OR ".join(category_parts) + ")" if category_parts else ""
    if main and category:
        return f"({main}) AND {category}"
    if main:
        return main
    if category:
        return category
    return "cat:math.DG OR cat:math.AG OR cat:math.CV"


def _escape_query_term(term: str) -> str:
    return term.replace('"', "")


def _normalize_sort_by(sort_by: str) -> str:
    if sort_by == "newest":
        return "submittedDate"
    if sort_by in {"relevance", "lastUpdatedDate", "submittedDate"}:
        return sort_by
    return "relevance"


def _text(entry: ET.Element, path: str) -> str | None:
    found = entry.find(path, ATOM_NS)
    return found.text if found is not None else None


def _normalize(text: str) -> str:
    return " ".join(text.split())


def _year_from_date(value: str | None) -> int | None:
    if not value:
        return None
    try:
        return datetime.fromisoformat(value.replace("Z", "+00:00")).year
    except ValueError:
        return None
