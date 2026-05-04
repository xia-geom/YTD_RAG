r"""Conservative search-only normalization for mathematical text and symbols.

The helpers in this module deliberately do not rewrite source content. They
produce metadata/search surfaces that make common mathematical variants easier
to retrieve while preserving the original LaTeX in chunks.
"""

from __future__ import annotations

import re
import unicodedata
from collections.abc import Iterable


COMMAND_DEFINITION_RE = re.compile(
    r"\\(?P<command>renewcommand|newcommand|providecommand|DeclareRobustCommand)\*?",
)
DOCUMENT_COMMAND_RE = re.compile(
    r"\\(?P<command>NewDocumentCommand|RenewDocumentCommand|ProvideDocumentCommand|DeclareDocumentCommand|DeclareExpandableDocumentCommand)\*?",
)
MATH_OPERATOR_RE = re.compile(r"\\DeclareMathOperator\*?")
DEF_RE = re.compile(r"\\(?P<command>gdef|xdef|edef|def)\b")
LET_RE = re.compile(r"\\let\b")
CONTROL_SEQUENCE_RE = re.compile(r"\\[A-Za-z]+|\\.")
SUBSCRIPT_RE = re.compile(r"(?P<base>\\?[A-Za-z]+)_\{?(?P<sub>[A-Za-z0-9]+)\}?")


def strip_accents(text: str) -> str:
    """Return ``text`` with Unicode combining marks removed."""

    decomposed = unicodedata.normalize("NFKD", text)
    return "".join(char for char in decomposed if not unicodedata.combining(char))


def normalize_search_text(text: str) -> str:
    """Normalize text for matching while keeping semantics conservative."""

    normalized = strip_accents(text)
    normalized = normalized.replace("–", "-").replace("—", "-").replace("−", "-")
    normalized = normalized.casefold()
    normalized = re.sub(r"\bmonge\s*[- ]\s*ampere\b", "monge-ampere", normalized)
    normalized = re.sub(r"\bk\s*[- ]?\s*energy\b|\bkenergy\b", "k-energy", normalized)
    normalized = re.sub(r"\bc\s*s\s*c\s*k\b", "csck", normalized)
    return normalized


def normalize_math_token(token: str) -> str:
    """Normalize one math/search token without identifying distinct variables."""

    stripped = token.strip()
    if not stripped:
        return ""
    if stripped.startswith("\\"):
        return stripped
    return _collapse_subscript(normalize_search_text(stripped))


def extract_latex_macro_aliases(text: str) -> dict[str, str]:
    r"""Extract simple zero-argument LaTeX macro aliases.

    Supported forms include::

        \newcommand{\E}{\mathcal{E}}
        \renewcommand\om{\omega}
        \DeclareMathOperator{\Ric}{Ric}
        \NewDocumentCommand{\dd}{}{\mathrm{d}}
        \def\K{\mathcal{K}}
        \let\eps=\epsilon

    Macros with arguments or replacement text containing ``#`` are skipped.
    Malformed definitions are ignored.
    """

    aliases: dict[str, str] = {}
    source = _strip_latex_comments(text)
    _extract_command_aliases(source, aliases)
    _extract_document_command_aliases(source, aliases)
    _extract_math_operator_aliases(source, aliases)
    _extract_def_aliases(source, aliases)
    _extract_let_aliases(source, aliases)
    return aliases


def expand_latex_symbols(symbols: list[str], aliases: dict[str, str]) -> list[str]:
    """Return raw symbols plus conservative aliases and normalized variants."""

    expanded: list[str] = []
    for symbol in symbols:
        _append(expanded, symbol)
        normalized = normalize_math_token(symbol)
        if normalized and normalized != symbol:
            _append(expanded, normalized)

        alias_key = symbol if symbol in aliases else _base_macro(symbol)
        if alias_key and alias_key in aliases:
            alias = aliases[alias_key]
            _append(expanded, alias)
            normalized_alias = normalize_math_token(alias)
            if normalized_alias and normalized_alias != alias:
                _append(expanded, normalized_alias)
    return expanded


def extract_concept_tags(text: str, symbols: list[str] | None = None) -> list[str]:
    """Extract broad retrieval concepts from text and normalized symbols."""

    normalized = normalize_search_text(text)
    symbol_text = " ".join(symbols or [])
    tags: list[str] = []

    if any(phrase in normalized for phrase in ("abreu equation", "symplectic potential", "moment polytope")):
        tags.append("abreu_toric")
    if "mabuchi" in normalized or "k-energy" in normalized or _contains_symbol(symbol_text, r"\mathcal{K}"):
        tags.append("mabuchi_k_energy")
    if "monge-ampere energy" in normalized or _contains_symbol(symbol_text, r"\mathcal{E}"):
        tags.append("monge_ampere_energy")
    if (
        "weak geodesic" in normalized
        or "finite energy" in normalized
        or "d1" in {normalize_math_token(symbol) for symbol in symbols or []}
    ):
        tags.append("finite_energy_geodesic")
    if "csck" in normalized or "constant scalar curvature kahler" in normalized:
        tags.append("csck")
    if "poincare" in normalized or "cusp" in normalized:
        tags.append("poincare_cusp")
    if "conic" in normalized or "cone angle" in normalized:
        tags.append("conic_metric")
    if "weighted mabuchi" in normalized or "lahdili" in normalized or "weighted extremal" in normalized:
        tags.append("weighted_extremal")

    return _dedupe(tags)


def search_metadata_for_content(
    content: str,
    symbols: list[str],
    aliases: dict[str, str] | None = None,
) -> dict[str, object]:
    """Build additive search metadata for a chunk."""

    aliases = aliases or {}
    normalized_symbols = expand_latex_symbols(symbols, aliases)
    return {
        "normalized_symbols": normalized_symbols,
        "concept_tags": extract_concept_tags(content, normalized_symbols),
        "macro_alias_count": len(aliases),
    }


def _collapse_subscript(token: str) -> str:
    return SUBSCRIPT_RE.sub(lambda match: f"{match.group('base')}{match.group('sub')}", token)


def _contains_symbol(symbol_text: str, symbol: str) -> bool:
    return symbol in symbol_text or normalize_search_text(symbol) in normalize_search_text(symbol_text)


def _extract_command_aliases(text: str, aliases: dict[str, str]) -> None:
    for match in COMMAND_DEFINITION_RE.finditer(text):
        pos = match.end()
        macro, pos = _read_macro_name(text, pos)
        if not macro:
            continue
        pos = _skip_ws(text, pos)
        if pos < len(text) and text[pos] == "[":
            optional, pos = _read_optional_group(text, pos)
            if optional is None:
                continue
            if optional.strip() not in {"", "0"}:
                continue
            pos = _skip_ws(text, pos)
            if pos < len(text) and text[pos] == "[":
                # Optional default value implies arguments in TeX syntax.
                continue
        replacement, _ = _read_required_group(text, pos)
        _record_alias(aliases, macro, replacement)


def _extract_document_command_aliases(text: str, aliases: dict[str, str]) -> None:
    for match in DOCUMENT_COMMAND_RE.finditer(text):
        macro, pos = _read_macro_name(text, match.end())
        if not macro:
            continue
        arg_spec, pos = _read_required_group(text, pos)
        if arg_spec is None or arg_spec.strip():
            continue
        replacement, _ = _read_required_group(text, pos)
        _record_alias(aliases, macro, replacement)


def _extract_math_operator_aliases(text: str, aliases: dict[str, str]) -> None:
    for match in MATH_OPERATOR_RE.finditer(text):
        macro, pos = _read_macro_name(text, match.end())
        if not macro:
            continue
        replacement, _ = _read_required_group(text, pos)
        _record_alias(aliases, macro, replacement)


def _extract_def_aliases(text: str, aliases: dict[str, str]) -> None:
    for match in DEF_RE.finditer(text):
        macro, pos = _read_direct_control_sequence(text, match.end())
        if not macro:
            continue
        group_start = _skip_ws(text, pos)
        if group_start > len(text) or (group_start < len(text) and text[group_start] != "{"):
            continue
        if "#" in text[pos:group_start]:
            continue
        replacement, _ = _read_required_group(text, group_start)
        _record_alias(aliases, macro, replacement)


def _extract_let_aliases(text: str, aliases: dict[str, str]) -> None:
    for match in LET_RE.finditer(text):
        macro, pos = _read_direct_control_sequence(text, match.end())
        if not macro:
            continue
        pos = _skip_ws(text, pos)
        if pos < len(text) and text[pos] == "=":
            pos += 1
        replacement, _ = _read_direct_control_sequence(text, pos)
        if replacement:
            _record_alias(aliases, macro, replacement)


def _record_alias(aliases: dict[str, str], macro: str, replacement: str | None) -> None:
    if not _is_simple_macro_name(macro) or replacement is None:
        return
    replacement = _clean_replacement(replacement)
    if not replacement or "#" in replacement or len(replacement) > 200:
        return
    if r"\begin" in replacement or r"\end" in replacement:
        return
    aliases[macro] = replacement


def _clean_replacement(replacement: str) -> str:
    return re.sub(r"\s+", " ", replacement.strip())


def _read_macro_name(text: str, pos: int) -> tuple[str | None, int]:
    pos = _skip_ws(text, pos)
    if pos < len(text) and text[pos] == "{":
        value, end = _read_required_group(text, pos)
        if value is None:
            return None, pos
        macro = value.strip()
        return (macro, end) if _is_simple_macro_name(macro) else (None, end)
    return _read_direct_control_sequence(text, pos)


def _read_direct_control_sequence(text: str, pos: int) -> tuple[str | None, int]:
    pos = _skip_ws(text, pos)
    match = CONTROL_SEQUENCE_RE.match(text, pos)
    if not match:
        return None, pos
    macro = match.group(0)
    return (macro, match.end()) if _is_simple_macro_name(macro) else (None, match.end())


def _is_simple_macro_name(value: str) -> bool:
    return bool(re.fullmatch(r"\\[A-Za-z]+", value.strip()))


def _read_required_group(text: str, pos: int) -> tuple[str | None, int]:
    pos = _skip_ws(text, pos)
    if pos >= len(text) or text[pos] != "{":
        return None, pos
    depth = 0
    content_start = pos + 1
    i = pos
    while i < len(text):
        char = text[i]
        if char == "\\":
            i += 2
            continue
        if char == "{":
            depth += 1
        elif char == "}":
            depth -= 1
            if depth == 0:
                return text[content_start:i], i + 1
        i += 1
    return None, pos


def _read_optional_group(text: str, pos: int) -> tuple[str | None, int]:
    pos = _skip_ws(text, pos)
    if pos >= len(text) or text[pos] != "[":
        return None, pos
    i = pos + 1
    while i < len(text):
        if text[i] == "\\":
            i += 2
            continue
        if text[i] == "]":
            return text[pos + 1 : i], i + 1
        i += 1
    return None, pos


def _skip_ws(text: str, pos: int) -> int:
    while pos < len(text) and text[pos].isspace():
        pos += 1
    return pos


def _base_macro(symbol: str) -> str | None:
    match = CONTROL_SEQUENCE_RE.match(symbol.strip())
    return match.group(0) if match else None


def _append(items: list[str], item: str | None) -> None:
    if item and item not in items:
        items.append(item)


def _dedupe(items: Iterable[str]) -> list[str]:
    seen: set[str] = set()
    result: list[str] = []
    for item in items:
        if item and item not in seen:
            seen.add(item)
            result.append(item)
    return result


def _strip_latex_comments(text: str) -> str:
    lines: list[str] = []
    for line in text.splitlines(keepends=True):
        cut = len(line)
        for index, char in enumerate(line):
            if char == "%" and not _is_escaped(line, index):
                cut = index
                break
        lines.append(line[:cut])
        if line.endswith(("\n", "\r")) and not lines[-1].endswith(("\n", "\r")):
            lines[-1] += "\n"
    return "".join(lines)


def _is_escaped(text: str, pos: int) -> bool:
    backslashes = 0
    index = pos - 1
    while index >= 0 and text[index] == "\\":
        backslashes += 1
        index -= 1
    return backslashes % 2 == 1
