"""LaTeX chunking that preserves mathematical structure."""

from __future__ import annotations

import hashlib
import re
from pathlib import Path

from .models import Chunk, DocumentMetadata
from .symbol_normalization import extract_latex_macro_aliases, search_metadata_for_content
from .text_cleaning import extract_symbols, normalize_whitespace


SECTION_LEVELS = {"section": 0, "subsection": 1, "subsubsection": 2}
SECTION_RE = re.compile(
    r"\\(?P<kind>section|subsection|subsubsection)\*?(?:\[[^\]]*\])?\{(?P<title>[^{}\n]*(?:\{[^{}\n]*\}[^{}\n]*)*)\}"
)

ENV_TO_CHUNK_TYPE = {
    "definition": "definition",
    "theorem": "theorem",
    "lemma": "lemma",
    "proposition": "proposition",
    "corollary": "theorem",
    "proof": "proof",
    "example": "example",
    "remark": "remark",
    "question": "question",
    "conjecture": "conjecture",
    "computation": "computation",
    "equation": "text",
    "align": "text",
}
STATIC_THEOREM_ALIASES = {
    "thm": "theorem",
    "theo": "theorem",
    "theorem": "theorem",
    "lem": "lemma",
    "lemma": "lemma",
    "prop": "proposition",
    "proposition": "proposition",
    "defn": "definition",
    "defi": "definition",
    "definition": "definition",
    "cor": "theorem",
    "corr": "theorem",
    "corollary": "theorem",
    "rem": "remark",
    "rmk": "remark",
    "remark": "remark",
    "remarks": "remark",
    "rmks": "remark",
    "ex": "example",
    "exmp": "example",
    "example": "example",
    "conj": "conjecture",
    "conjecture": "conjecture",
    "ques": "question",
    "quest": "question",
    "question": "question",
    "claim": "theorem",
    "proof": "proof",
}
ENV_NAMES = tuple(sorted(ENV_TO_CHUNK_TYPE, key=len, reverse=True))
BEGIN_ENV_RE = re.compile(r"\\begin\{(?P<env>" + "|".join(ENV_NAMES) + r")\*?\}")
NEWTHEOREM_RE = re.compile(
    r"""
    \\newtheorem\*?                 # \newtheorem or \newtheorem*
    \s*\{\s*(?P<env>[^{}\[\]\s]+)\s*\}
    \s*(?:\[[^\]]*\])?             # optional shared counter
    \s*\{\s*(?P<display>[^{}]*(?:\{[^{}]*\}[^{}]*)*)\s*\}
    \s*(?:\[[^\]]*\])?             # optional trailing numbering scope
    """,
    re.IGNORECASE | re.VERBOSE,
)


def make_chunk_id(source_path: str, line_start: int | None, line_end: int | None, chunk_type: str, content: str) -> str:
    digest = hashlib.sha1(
        f"{source_path}:{line_start}:{line_end}:{chunk_type}:{content[:120]}".encode("utf-8")
    ).hexdigest()[:16]
    return f"chunk-{digest}"


def _section_title(raw: str) -> str:
    return normalize_whitespace(raw.replace("\n", " "))


def _update_section_path(section_path: list[str], kind: str, title: str) -> list[str]:
    level = SECTION_LEVELS[kind]
    next_path = section_path[:level]
    next_path.append(title)
    return next_path


def _canonical_newtheorem_chunk_type(display_name: str) -> str | None:
    normalized = normalize_whitespace(re.sub(r"\\[a-zA-Z]+\*?", " ", display_name).lower())
    if "definition" in normalized:
        return "definition"
    if "proposition" in normalized:
        return "proposition"
    if "lemma" in normalized:
        return "lemma"
    if "corollary" in normalized:
        return "theorem"
    if "theorem" in normalized or "claim" in normalized:
        return "theorem"
    if "remark" in normalized:
        return "remark"
    if "example" in normalized:
        return "example"
    if "conjecture" in normalized:
        return "conjecture"
    if "question" in normalized:
        return "question"
    if "computation" in normalized:
        return "computation"
    return None


def extract_newtheorem_aliases(text: str) -> dict[str, str]:
    """Return valid chunk-type aliases declared by LaTeX \\newtheorem commands."""

    aliases: dict[str, str] = {}
    for match in NEWTHEOREM_RE.finditer(text):
        chunk_type = _canonical_newtheorem_chunk_type(match.group("display"))
        if chunk_type is not None:
            aliases[match.group("env")] = chunk_type
    return aliases


def _begin_env_re(env_to_chunk_type: dict[str, str]) -> re.Pattern[str]:
    env_names = tuple(sorted(env_to_chunk_type, key=len, reverse=True))
    return re.compile(r"\\begin\{(?P<env>" + "|".join(re.escape(env) for env in env_names) + r")\*?\}")


def chunk_latex_text(
    text: str,
    source_path: str,
    metadata: DocumentMetadata | None = None,
    max_text_chars: int = 3000,
) -> list[Chunk]:
    """Split LaTeX source into section-aware theorem/proof/example chunks."""

    env_to_chunk_type = dict(ENV_TO_CHUNK_TYPE)
    env_to_chunk_type.update(STATIC_THEOREM_ALIASES)
    env_to_chunk_type.update(extract_newtheorem_aliases(text))
    begin_env_re = _begin_env_re(env_to_chunk_type)
    lines = text.splitlines(keepends=True)
    chunks: list[Chunk] = []
    section_path: list[str] = []
    buffer: list[tuple[int, str]] = []
    title = metadata.title if metadata else None
    topics = list(metadata.topics) if metadata else []
    macro_aliases = extract_latex_macro_aliases(text)

    def chunk_metadata(content: str, symbols: list[str], environment: str | None = None) -> dict[str, object]:
        values: dict[str, object] = {"source_format": "latex"}
        if environment is not None:
            values["environment"] = environment
        values.update(search_metadata_for_content(content, symbols, macro_aliases))
        return values

    def flush_text_buffer() -> None:
        nonlocal buffer
        if not buffer:
            return

        group: list[tuple[int, str]] = []

        def emit_group(items: list[tuple[int, str]]) -> None:
            if not items:
                return
            content = "".join(line for _, line in items).strip()
            if not content:
                return
            line_start = items[0][0]
            line_end = items[-1][0]
            symbols = extract_symbols(content)
            chunks.append(
                Chunk(
                    chunk_id=make_chunk_id(source_path, line_start, line_end, "text", content),
                    source_path=source_path,
                    title=title,
                    chunk_type="text",
                    section_path=list(section_path),
                    line_start=line_start,
                    line_end=line_end,
                    content=content,
                    metadata=chunk_metadata(content, symbols),
                    symbols=symbols,
                    topics=topics,
                )
            )

        current_len = 0
        for item in buffer:
            group.append(item)
            current_len += len(item[1])
            if current_len >= max_text_chars and not item[1].strip():
                emit_group(group)
                group = []
                current_len = 0
        emit_group(group)
        buffer = []

    i = 0
    while i < len(lines):
        line_no = i + 1
        line = lines[i]
        section_match = SECTION_RE.search(line)
        env_match = begin_env_re.search(line)

        if section_match and (not env_match or section_match.start() < env_match.start()):
            flush_text_buffer()
            section_path = _update_section_path(
                section_path,
                section_match.group("kind"),
                _section_title(section_match.group("title")),
            )
            buffer.append((line_no, line))
            i += 1
            continue

        if env_match:
            flush_text_buffer()
            env_name = env_match.group("env")
            begin_same_env_re = re.compile(r"\\begin\{" + re.escape(env_name) + r"\*?\}")
            end_re = re.compile(r"\\end\{" + re.escape(env_name) + r"\*?\}")
            env_lines: list[tuple[int, str]] = [(line_no, line)]
            # Track only the current environment. Other environments nested
            # inside a theorem/proof should remain part of that larger chunk.
            depth = 1 + len(begin_same_env_re.findall(line[env_match.end() :]))
            depth -= len(end_re.findall(line[env_match.end() :]))
            i += 1
            while i < len(lines) and depth > 0:
                next_line_no = i + 1
                next_line = lines[i]
                env_lines.append((next_line_no, next_line))
                depth += len(begin_same_env_re.findall(next_line))
                depth -= len(end_re.findall(next_line))
                i += 1

            content = "".join(raw for _, raw in env_lines).strip()
            chunk_type = env_to_chunk_type.get(env_name, "text")
            symbols = extract_symbols(content)
            chunks.append(
                Chunk(
                    chunk_id=make_chunk_id(source_path, env_lines[0][0], env_lines[-1][0], chunk_type, content),
                    source_path=source_path,
                    title=title,
                    chunk_type=chunk_type,  # type: ignore[arg-type]
                    section_path=list(section_path),
                    line_start=env_lines[0][0],
                    line_end=env_lines[-1][0],
                    content=content,
                    metadata=chunk_metadata(content, symbols, env_name),
                    symbols=symbols,
                    topics=topics,
                )
            )
            continue

        buffer.append((line_no, line))
        if sum(len(raw) for _, raw in buffer) >= max_text_chars and not line.strip():
            flush_text_buffer()
        i += 1

    flush_text_buffer()
    return chunks


def chunk_latex_file(path: str | Path, metadata: DocumentMetadata | None = None) -> list[Chunk]:
    source_path = str(path)
    text = Path(path).read_text(encoding="utf-8", errors="replace")
    return chunk_latex_text(text, source_path=source_path, metadata=metadata)
