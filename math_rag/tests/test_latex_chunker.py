from math_rag.latex_chunker import chunk_latex_text
from math_rag.models import DocumentMetadata


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
