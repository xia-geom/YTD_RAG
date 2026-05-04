from math_rag.symbol_normalization import (
    expand_latex_symbols,
    extract_concept_tags,
    extract_latex_macro_aliases,
    normalize_math_token,
    normalize_search_text,
    strip_accents,
)


def test_strip_accents_preserves_plain_letters():
    assert strip_accents("Poincaré Kähler Monge-Ampère") == "Poincare Kahler Monge-Ampere"


def test_normalize_search_text_matches_accents_and_spellings():
    assert normalize_search_text("Poincaré type") == normalize_search_text("poincare type")
    assert normalize_search_text("Kähler geometry") == normalize_search_text("kahler geometry")
    assert normalize_search_text("Monge-Ampère energy") == normalize_search_text("monge ampere energy")
    assert normalize_search_text("cscK") == "csck"
    assert normalize_search_text("K energy") == normalize_search_text("kenergy")


def test_extract_latex_macro_aliases_handles_common_zero_argument_forms():
    text = r"""
\newcommand{\E}{\mathcal{E}}
\renewcommand{\om}{\omega}
\providecommand\K{\mathcal{K}}
\DeclareRobustCommand{\MA}{\mathrm{MA}}
\DeclareMathOperator{\Ric}{Ric}
\DeclareMathOperator*{\Argmax}{arg\,max}
\NewDocumentCommand{\dd}{}{\mathrm{d}}
\def\Scal{\mathrm{Scal}}
\let\eps=\epsilon
"""
    aliases = extract_latex_macro_aliases(text)

    assert aliases[r"\E"] == r"\mathcal{E}"
    assert aliases[r"\om"] == r"\omega"
    assert aliases[r"\K"] == r"\mathcal{K}"
    assert aliases[r"\MA"] == r"\mathrm{MA}"
    assert aliases[r"\Ric"] == "Ric"
    assert aliases[r"\Argmax"] == r"arg\,max"
    assert aliases[r"\dd"] == r"\mathrm{d}"
    assert aliases[r"\Scal"] == r"\mathrm{Scal}"
    assert aliases[r"\eps"] == r"\epsilon"


def test_extract_latex_macro_aliases_skips_argument_macros_and_comments():
    text = r"""
% \newcommand{\Commented}{\mathcal{C}}
\newcommand{\foo}[1]{#1}
\renewcommand{\bar}[2]{#1+#2}
\DeclareDocumentCommand{\baz}{m}{#1}
\def\bad#1{#1}
\newcommand{\good}[0]{\mathcal{G}}
"""
    aliases = extract_latex_macro_aliases(text)

    assert r"\Commented" not in aliases
    assert r"\foo" not in aliases
    assert r"\bar" not in aliases
    assert r"\baz" not in aliases
    assert r"\bad" not in aliases
    assert aliases[r"\good"] == r"\mathcal{G}"


def test_expand_latex_symbols_keeps_originals_and_adds_aliases():
    expanded = expand_latex_symbols(
        [r"\E", r"\K", r"\om", r"\MA", "d_1", "d_{1}"],
        {r"\E": r"\mathcal{E}", r"\K": r"\mathcal{K}", r"\om": r"\omega", r"\MA": r"\mathrm{MA}"},
    )

    assert r"\E" in expanded
    assert r"\mathcal{E}" in expanded
    assert r"\K" in expanded
    assert r"\mathcal{K}" in expanded
    assert r"\om" in expanded
    assert r"\omega" in expanded
    assert r"\MA" in expanded
    assert r"\mathrm{MA}" in expanded
    assert "d_1" in expanded
    assert "d1" in expanded


def test_normalize_math_token_collapses_simple_non_latex_subscripts_only():
    assert normalize_math_token("d_1") == "d1"
    assert normalize_math_token("d_{1}") == "d1"
    assert normalize_math_token(r"\E_v") == r"\E_v"


def test_extract_concept_tags_for_core_geometry_terms():
    assert "abreu_toric" in extract_concept_tags("The Abreu equation uses a symplectic potential.")
    assert "mabuchi_k_energy" in extract_concept_tags("The Mabuchi K-energy is coercive.")
    assert "finite_energy_geodesic" in extract_concept_tags("A weak geodesic has finite energy d_1 control.", ["d1"])
    assert "poincare_cusp" in extract_concept_tags("A Poincaré type cusp metric.")
    assert "conic_metric" in extract_concept_tags("The cone angle defines a conic metric.")
    assert "weighted_extremal" in extract_concept_tags("Lahdili weighted extremal metrics.")
