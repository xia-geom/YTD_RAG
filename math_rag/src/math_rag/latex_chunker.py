"""LaTeX chunking that preserves mathematical structure."""

from __future__ import annotations

import hashlib
import re
from pathlib import Path

from .models import Chunk, DocumentMetadata
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
ENV_NAMES = tuple(sorted(ENV_TO_CHUNK_TYPE, key=len, reverse=True))
BEGIN_ENV_RE = re.compile(r"\\begin\{(?P<env>" + "|".join(ENV_NAMES) + r")\*?\}")


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


def chunk_latex_text(
    text: str,
    source_path: str,
    metadata: DocumentMetadata | None = None,
    max_text_chars: int = 3000,
) -> list[Chunk]:
    """Split LaTeX source into section-aware theorem/proof/example chunks."""

    lines = text.splitlines(keepends=True)
    chunks: list[Chunk] = []
    section_path: list[str] = []
    buffer: list[tuple[int, str]] = []
    title = metadata.title if metadata else None
    topics = list(metadata.topics) if metadata else []

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
                    metadata={"source_format": "latex"},
                    symbols=extract_symbols(content),
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
        env_match = BEGIN_ENV_RE.search(line)

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
            chunk_type = ENV_TO_CHUNK_TYPE.get(env_name, "text")
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
                    metadata={"source_format": "latex", "environment": env_name},
                    symbols=extract_symbols(content),
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
