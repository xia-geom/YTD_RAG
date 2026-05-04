"""Small text utilities that preserve mathematical notation."""

from __future__ import annotations

import re
from collections.abc import Iterable

from .symbol_normalization import normalize_search_text


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
LATEX_COMMAND_NAME_RE = re.compile(r"^\\[A-Za-z]+")
UNICODE_MATH_SYMBOL_RE = re.compile(r"[\u0391-\u03A9\u03B1-\u03C9\u03D1-\u03D6]")

STRUCTURAL_LATEX_COMMANDS = {
    r"\begin",
    r"\end",
    r"\section",
    r"\subsection",
    r"\subsubsection",
    r"\chapter",
    r"\part",
    r"\paragraph",
    r"\subparagraph",
    r"\appendix",
    r"\label",
    r"\ref",
    r"\eqref",
    r"\cite",
    r"\citet",
    r"\citep",
    r"\bibliographystyle",
    r"\bibliography",
    r"\documentclass",
    r"\usepackage",
    r"\title",
    r"\author",
    r"\date",
    r"\maketitle",
    r"\tableofcontents",
    r"\caption",
    r"\footnote",
    r"\url",
    r"\href",
    r"\newcommand",
    r"\renewcommand",
    r"\providecommand",
    r"\DeclareMathOperator",
    r"\newtheorem",
    r"\theoremstyle",
    r"\item",
    r"\it",
    r"\rm",
    r"\bf",
    r"\em",
    r"\emph",
    r"\textbf",
    r"\textit",
    r"\textsc",
    r"\texttt",
}


def normalize_whitespace(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip()


def tokenize(text: str) -> list[str]:
    """Tokenize without destroying LaTeX commands or compact symbols."""

    normalized = normalize_search_text(text)
    return [token.lower() for token in TOKEN_RE.findall(normalized) if token.strip()]


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
    symbols = [symbol for symbol in LATEX_SYMBOL_RE.findall(text) if not _is_structural_latex_symbol(symbol)]
    symbols.extend(MATH_WORD_RE.findall(text))
    symbols.extend(UNICODE_MATH_SYMBOL_RE.findall(text))
    for raw in re.findall(r"\$([^$]{1,80})\$", text):
        symbols.extend(
            token
            for token in raw.split()
            if any(ch in token for ch in "\\_^{}") and not _is_structural_latex_symbol(token)
        )
    return dedupe_preserve_order(symbols)[:40]


def _is_structural_latex_symbol(symbol: str) -> bool:
    match = LATEX_COMMAND_NAME_RE.match(symbol.strip())
    return bool(match and match.group(0) in STRUCTURAL_LATEX_COMMANDS)


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

    normalized_text = normalize_search_text(text)
    terms = salient_terms(query) or tokenize(query)
    positions = [
        normalized_text.find(normalize_search_text(term))
        for term in terms
        if normalized_text.find(normalize_search_text(term)) >= 0
    ]
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
