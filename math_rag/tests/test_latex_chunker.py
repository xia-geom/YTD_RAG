from math_rag.latex_chunker import chunk_latex_text
from math_rag.models import DocumentMetadata


def _find_chunk_by_environment(text: str, environment: str):
    chunks = chunk_latex_text(text, "notes.tex")
    return next(chunk for chunk in chunks if chunk.metadata.get("environment") == environment)


def test_latex_chunker_detects_theorem_proof_example_environments():
    text = r"""
\section{Toric setup}
Some setup text.
\begin{theorem}\label{thm:cc}
Assume the Chen-Cheng estimates. Then a cscK statement is discussed.
\end{theorem}
\begin{proof}
The proof uses the Mabuchi energy and weak geodesics.
\end{proof}
\begin{example}
For CP1, use the polytope $[-1,1]$ and cone angle $\beta$.
\end{example}
"""
    metadata = DocumentMetadata(source_path="notes.tex", title="Notes", topics=["cscK"])
    chunks = chunk_latex_text(text, "notes.tex", metadata)
    types = [chunk.chunk_type for chunk in chunks]

    assert "theorem" in types
    assert "proof" in types
    assert "example" in types

    theorem = next(chunk for chunk in chunks if chunk.chunk_type == "theorem")
    proof = next(chunk for chunk in chunks if chunk.chunk_type == "proof")
    example = next(chunk for chunk in chunks if chunk.chunk_type == "example")

    assert theorem.section_path == ["Toric setup"]
    assert r"\label{thm:cc}" in theorem.content
    assert r"\begin{proof}" not in theorem.content
    assert "Mabuchi energy" in proof.content
    assert r"\begin{example}" not in proof.content
    assert r"\beta" in example.content
    assert theorem.line_start is not None
    assert theorem.line_end is not None
    assert theorem.line_end < proof.line_start < proof.line_end < example.line_start


def test_latex_chunker_detects_static_theorem_alias():
    text = r"""\begin{thm}
Statement.
\end{thm}
"""

    theorem = _find_chunk_by_environment(text, "thm")

    assert theorem.chunk_type == "theorem"
    assert theorem.content.startswith(r"\begin{thm}")


def test_latex_chunker_detects_simple_newtheorem_alias():
    text = r"""\newtheorem{thm}{Theorem}
\begin{thm}
Statement.
\end{thm}
"""

    theorem = _find_chunk_by_environment(text, "thm")

    assert theorem.chunk_type == "theorem"


def test_latex_chunker_detects_newtheorem_shared_counter_alias():
    text = r"""\newtheorem{lem}[thm]{Lemma}
\begin{lem}
Lemma statement.
\end{lem}
"""

    lemma = _find_chunk_by_environment(text, "lem")

    assert lemma.chunk_type == "lemma"


def test_latex_chunker_detects_newtheorem_equation_counter_alias():
    text = r"""\newtheorem{prop}[equation]{Proposition}
\begin{prop}
Proposition statement.
\end{prop}
"""

    proposition = _find_chunk_by_environment(text, "prop")

    assert proposition.chunk_type == "proposition"


def test_latex_chunker_detects_starred_newtheorem_alias():
    text = r"""\newtheorem*{obs}{Remark}
\begin{obs}
Remark text.
\end{obs}
"""

    remark = _find_chunk_by_environment(text, "obs")

    assert remark.chunk_type == "remark"


def test_latex_chunker_detects_starred_newtheorem_remark_environment():
    text = r"""\newtheorem*{remark}{Remark}
\begin{remark}
Remark text.
\end{remark}
"""

    remark = _find_chunk_by_environment(text, "remark")

    assert remark.chunk_type == "remark"


def test_latex_chunker_detects_newtheorem_trailing_numbering_alias():
    text = r"""\newtheorem{defn}{Definition}[section]
\begin{defn}
Definition text.
\end{defn}
"""

    definition = _find_chunk_by_environment(text, "defn")

    assert definition.chunk_type == "definition"


def test_latex_chunker_maps_corollary_alias_to_theorem():
    text = r"""\newtheorem{cor}[thm]{Corollary}
\begin{cor}
Corollary text.
\end{cor}
"""

    corollary = _find_chunk_by_environment(text, "cor")

    assert corollary.chunk_type == "theorem"


def test_latex_chunker_maps_claim_alias_to_valid_type():
    text = r"""\newtheorem{claim}{Claim}
\begin{claim}
Claim text.
\end{claim}
"""

    claim = _find_chunk_by_environment(text, "claim")

    assert claim.chunk_type == "theorem"


def test_latex_chunker_leaves_unknown_environment_as_text():
    text = r"""\begin{weirdenv}
Some content.
\end{weirdenv}
"""

    chunks = chunk_latex_text(text, "notes.tex")

    assert [chunk.chunk_type for chunk in chunks] == ["text"]
    assert chunks[0].metadata["source_format"] == "latex"
    assert "environment" not in chunks[0].metadata


def test_latex_chunker_preserves_alias_line_numbers():
    text = """Intro line.
Another line.
\\begin{thm}
Statement.
\\end{thm}
"""

    theorem = _find_chunk_by_environment(text, "thm")

    assert theorem.line_start == 3
    assert theorem.line_end == 5


def test_latex_chunker_preserves_alias_section_path():
    text = r"""\section{Main Results}
\newtheorem{thm}{Theorem}
\begin{thm}
Statement.
\end{thm}
"""

    theorem = _find_chunk_by_environment(text, "thm")

    assert theorem.section_path == ["Main Results"]


def test_latex_chunker_adds_search_metadata_without_rewriting_content():
    text = r"""
\newcommand{\E}{\mathcal{E}}
\newcommand{\K}{\mathcal{K}}
\newcommand{\om}{\omega}
\begin{thm}
The Poincaré cusp case studies the Mabuchi K-energy $\K$ and $\E_v$.
\end{thm}
"""

    theorem = _find_chunk_by_environment(text, "thm")

    assert r"\E_v" in theorem.content
    assert theorem.metadata["macro_alias_count"] == 3
    assert r"\begin{thm}" not in theorem.symbols
    assert r"\end{thm}" not in theorem.symbols
    assert r"\E" in theorem.symbols
    assert r"\mathcal{E}" in theorem.metadata["normalized_symbols"]
    assert r"\K" in theorem.metadata["normalized_symbols"]
    assert r"\mathcal{K}" in theorem.metadata["normalized_symbols"]
    assert "mabuchi_k_energy" in theorem.metadata["concept_tags"]
    assert "poincare_cusp" in theorem.metadata["concept_tags"]


def test_latex_chunker_preserves_user_macro_alias_expansion_after_symbol_filtering():
    text = r"""
\newcommand{\mE}{\mathcal{E}}
We study $\mE_v$.
"""

    chunks = chunk_latex_text(text, "notes.tex")
    chunk = chunks[0]

    assert r"\mE_v" in chunk.content
    assert r"\mE" in chunk.metadata["normalized_symbols"]
    assert r"\mathcal{E}" in chunk.metadata["normalized_symbols"]
    assert r"\newcommand" not in chunk.symbols
    assert r"\newcommand{\mE}" not in chunk.symbols
