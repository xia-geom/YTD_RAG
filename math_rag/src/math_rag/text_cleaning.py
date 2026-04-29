"""Small text utilities that preserve mathematical notation."""

from __future__ import annotations

import re
from collections.abc import Iterable


STOPWORDS = {
    "about",
    "after",
    "also",
    "and",
    "are",
    "between",
    "does",
    "find",
    "for",
    "from",
    "how",
    "into",
    "lemma",
    "material",
    "missing",
    "notes",
    "of",
    "on",
    "or",
    "proof",
    "prove",
    "proposition",
    "related",
    "result",
    "say",
    "show",
    "source",
    "sources",
    "statement",
    "the",
    "theorem",
    "their",
    "there",
    "these",
    "this",
    "to",
    "what",
    "where",
    "with",
}

TOKEN_RE = re.compile(
    r"""
    \\[A-Za-z]+(?:\*|\{[^{}\n]*\})?   # LaTeX command, sometimes with one simple argument
    |[A-Za-z]+(?:[-'][A-Za-z0-9]+)*     # words and names such as Chen-Cheng
    |\d+(?:\.\d+)?
    |\[[^\]\n]{1,40}\]                 # compact intervals such as [-1,1]
    |[^\s]                              # symbols
    """,
    re.VERBOSE,
)

LATEX_SYMBOL_RE = re.compile(r"\\[A-Za-z]+(?:\{[^{}\n]*\})?")
MATH_WORD_RE = re.compile(r"\b[A-Z][A-Za-z]+(?:-[A-Z][A-Za-z]+)+\b")


def normalize_whitespace(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip()


def tokenize(text: str) -> list[str]:
    """Tokenize without destroying LaTeX commands or compact symbols."""

    return [token.lower() for token in TOKEN_RE.findall(text) if token.strip()]


def salient_terms(text: str) -> list[str]:
    terms: list[str] = []
    for token in tokenize(text):
        plain = token.strip(".,;:(){}[]")
        if len(plain) >= 4 and plain not in STOPWORDS:
            terms.append(plain)
        elif "\\" in token or "-" in token:
            terms.append(token)
    return dedupe_preserve_order(terms)


def extract_symbols(text: str) -> list[str]:
    symbols = LATEX_SYMBOL_RE.findall(text)
    symbols.extend(MATH_WORD_RE.findall(text))
    for raw in re.findall(r"\$([^$]{1,80})\$", text):
        symbols.extend(token for token in raw.split() if any(ch in token for ch in "\\_^{}"))
    return dedupe_preserve_order(symbols)[:40]


def dedupe_preserve_order(items: Iterable[str]) -> list[str]:
    seen: set[str] = set()
    result: list[str] = []
    for item in items:
        if item and item not in seen:
            seen.add(item)
            result.append(item)
    return result


def make_snippet(content: str, query: str, max_chars: int = 360) -> str:
    text = normalize_whitespace(content)
    if len(text) <= max_chars:
        return text

    lower = text.lower()
    terms = salient_terms(query) or tokenize(query)
    positions = [lower.find(term.lower()) for term in terms if lower.find(term.lower()) >= 0]
    if positions:
        center = min(positions)
        start = max(0, center - max_chars // 3)
    else:
        start = 0
    end = min(len(text), start + max_chars)
    snippet = text[start:end].strip()
    if start > 0:
        snippet = "..." + snippet
    if end < len(text):
        snippet += "..."
    return snippet
