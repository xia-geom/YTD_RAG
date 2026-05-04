from math_rag.text_cleaning import extract_symbols, make_snippet, salient_terms, tokenize


def test_tokenize_is_accent_insensitive_for_core_terms():
    assert "poincare" in tokenize("Poincaré metric")
    assert "kahler" in tokenize("Kähler geometry")
    assert "monge-ampere" in tokenize("Monge-Ampère energy")
    assert tokenize("cscK") == ["csck"]


def test_salient_terms_normalizes_k_energy_variants():
    assert salient_terms("K energy coercivity") == salient_terms("kenergy coercivity")


def test_make_snippet_matches_poincare_query_but_preserves_original_text():
    content = "Intro. " + ("irrelevant text. " * 20) + "The Poincaré type metric is complete near D."

    snippet = make_snippet(content, "Poincare metric", max_chars=90)

    assert "Poincaré type metric" in snippet


def test_make_snippet_matches_kahler_query_but_preserves_original_text():
    content = "Intro. " + ("background text. " * 20) + "Kähler geometry controls the scalar curvature."

    snippet = make_snippet(content, "Kahler", max_chars=80)

    assert "Kähler geometry" in snippet


def test_extract_symbols_removes_structural_latex_commands():
    text = r"""
\section{Intro}
\begin{theorem}
\label{thm:main}
{\it Text} \cite{BDL}.
\end{theorem}
"""

    symbols = extract_symbols(text)

    assert r"\section" not in symbols
    assert r"\section{Intro}" not in symbols
    assert r"\begin" not in symbols
    assert r"\begin{theorem}" not in symbols
    assert r"\label" not in symbols
    assert r"\label{thm:main}" not in symbols
    assert r"\cite" not in symbols
    assert r"\cite{BDL}" not in symbols
    assert r"\it" not in symbols
    assert r"\end" not in symbols
    assert r"\end{theorem}" not in symbols


def test_extract_symbols_preserves_math_latex_commands():
    text = r"""
Let $\omega$, $\Omega$, $\varphi$, $\mathcal{E}$, $\mathcal{K}$,
$\mathrm{Ric}$, and $\operatorname{MA}$ appear.
"""

    symbols = extract_symbols(text)

    assert r"\omega" in symbols
    assert r"\Omega" in symbols
    assert r"\varphi" in symbols
    assert r"\mathcal{E}" in symbols
    assert r"\mathcal{K}" in symbols
    assert r"\mathrm{Ric}" in symbols
    assert r"\operatorname{MA}" in symbols


def test_extract_symbols_preserves_unicode_greek_symbols():
    symbols = extract_symbols("cone angle β and form ω")

    assert "β" in symbols
    assert "ω" in symbols
