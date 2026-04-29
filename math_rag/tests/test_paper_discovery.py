import io
import tarfile

from math_rag.arxiv_client import ArxivPaper, parse_arxiv_atom
from math_rag.downloader import download_approved_papers
from math_rag.loaders import discover_files
from math_rag.paper_ranker import DiscoveryConfig, rank_paper
from math_rag.paper_store import (
    PaperCandidate,
    is_duplicate,
    load_yaml_file,
    metadata_path,
    paper_dir,
    safe_arxiv_dirname,
    write_candidates,
    write_yaml_file,
)


ATOM = """<?xml version="1.0" encoding="UTF-8"?>
<feed xmlns="http://www.w3.org/2005/Atom" xmlns:arxiv="http://arxiv.org/schemas/atom">
  <entry>
    <id>http://arxiv.org/abs/2301.12345v2</id>
    <updated>2023-02-01T00:00:00Z</updated>
    <published>2023-01-01T00:00:00Z</published>
    <title>Toric cscK metrics and Mabuchi energy</title>
    <summary>We discuss the Abreu equation and cone angle limits.</summary>
    <author><name>Author A</name></author>
    <author><name>Darvas B</name></author>
    <category term="math.DG" scheme="http://arxiv.org/schemas/atom"/>
    <link title="pdf" href="https://arxiv.org/pdf/2301.12345v2" rel="related" type="application/pdf"/>
  </entry>
</feed>
"""


class FakeDownloadClient:
    def __init__(self, source_bytes=None, pdf_bytes=b"%PDF fake", fail_source=False, fail_pdf=False):
        self.source_bytes = source_bytes if source_bytes is not None else _tar_bytes({"main.tex": "\\section{A}\nText"})
        self.pdf_bytes = pdf_bytes
        self.fail_source = fail_source
        self.fail_pdf = fail_pdf
        self.urls = []

    def download_bytes(self, url):
        self.urls.append(url)
        if "e-print" in url:
            if self.fail_source:
                raise RuntimeError("no source")
            return self.source_bytes
        if self.fail_pdf:
            raise RuntimeError("no pdf")
        return self.pdf_bytes


def test_arxiv_metadata_parsing():
    papers = parse_arxiv_atom(ATOM)

    assert len(papers) == 1
    paper = papers[0]
    assert paper.arxiv_id == "2301.12345"
    assert paper.version == "v2"
    assert paper.title == "Toric cscK metrics and Mabuchi energy"
    assert paper.authors == ["Author A", "Darvas B"]
    assert paper.year == 2023
    assert paper.categories == ["math.DG"]
    assert paper.source_url.endswith("/2301.12345v2")
    assert paper.pdf_url.endswith("/2301.12345v2")


def test_candidate_ranking_by_keyword_and_author():
    paper = parse_arxiv_atom(ATOM)[0]
    candidate = rank_paper(paper, DiscoveryConfig(), query="Mabuchi energy")

    assert candidate.score > 0
    assert any("matched keyword: Mabuchi energy" in reason for reason in candidate.ranking_reasons)
    assert any("matched seed author: Darvas" in reason for reason in candidate.ranking_reasons)


def test_manual_blacklist_lowers_score_and_whitelist_raises_score():
    paper = ArxivPaper(
        arxiv_id="9999.00001",
        version="v1",
        title="A neutral note",
        authors=["Unmatched Author"],
        abstract="No configured terminology appears here.",
        year=2001,
        categories=["math.OA"],
    )
    base = rank_paper(paper, DiscoveryConfig())
    blacklisted = rank_paper(paper, DiscoveryConfig(manual_blacklist=["9999.00001"]))
    whitelisted = rank_paper(paper, DiscoveryConfig(manual_whitelist=["9999.00001"]))

    assert blacklisted.score < base.score
    assert any("manual blacklist penalty" in reason for reason in blacklisted.ranking_reasons)
    assert whitelisted.score > base.score
    assert any("manual whitelist bonus" in reason for reason in whitelisted.ranking_reasons)


def test_storage_path_generation_and_duplicate_detection(tmp_path):
    candidate = _candidate("2301.12345", action="download")
    assert safe_arxiv_dirname("2301.12345") == "2301.12345"
    assert paper_dir(tmp_path, "2301.12345") == tmp_path / "2301.12345"

    path = metadata_path(tmp_path, candidate.arxiv_id)
    write_yaml_file(path, {"arxiv_id": "2301.12345", "version": "v2"})

    assert is_duplicate(candidate, tmp_path)


def test_approved_only_download_behavior_and_no_mass_download_by_default(tmp_path):
    approved = _candidate("2301.12345", action="download")
    pending = _candidate("2301.54321", action="pending")
    candidates_path = tmp_path / "discovered.yaml"
    write_candidates(candidates_path, [approved, pending])

    results = download_approved_papers(str(candidates_path), corpus_arxiv_dir=str(tmp_path / "arxiv"), client=FakeDownloadClient())

    assert len(results) == 1
    assert results[0].arxiv_id == "2301.12345"
    assert (tmp_path / "arxiv" / "2301.12345" / "source" / "main.tex").exists()
    assert not (tmp_path / "arxiv" / "2301.54321").exists()

    pending_only = tmp_path / "pending.yaml"
    write_candidates(pending_only, [pending])
    assert download_approved_papers(str(pending_only), corpus_arxiv_dir=str(tmp_path / "none"), client=FakeDownloadClient()) == []
    assert (
        download_approved_papers(
            str(pending_only),
            corpus_arxiv_dir=str(tmp_path / "auto_blocked"),
            auto_download=True,
            client=FakeDownloadClient(),
        )
        == []
    )


def test_auto_download_can_only_include_pending_when_config_allows_it(tmp_path):
    pending = _candidate("2301.54321", action="pending")
    candidates_path = tmp_path / "pending.yaml"
    config_path = tmp_path / "config.yaml"
    write_candidates(candidates_path, [pending])
    write_yaml_file(config_path, {"download_policy": {"require_approval": False, "delay_seconds_between_requests": 0}})

    results = download_approved_papers(
        str(candidates_path),
        corpus_arxiv_dir=str(tmp_path / "auto_allowed"),
        config_path=str(config_path),
        auto_download=True,
        client=FakeDownloadClient(),
    )

    assert len(results) == 1
    assert results[0].arxiv_id == "2301.54321"


def test_tex_preferred_ingestion_file_selection(tmp_path):
    root = tmp_path / "corpus" / "arxiv" / "2301.12345"
    (root / "source").mkdir(parents=True)
    (root / "source" / "main.tex").write_text("\\section{Toric}\n", encoding="utf-8")
    (root / "paper.pdf").write_bytes(b"%PDF")
    write_yaml_file(root / "metadata.yaml", {"arxiv_id": "2301.12345", "primary_ingestion": "tex", "source_available": True})

    files = discover_files(tmp_path / "corpus")

    assert root / "source" / "main.tex" in files
    assert root / "paper.pdf" not in files


def test_pdf_fallback_and_metadata_only_ingestion_file_selection(tmp_path):
    pdf_root = tmp_path / "corpus" / "arxiv" / "2301.12345"
    (pdf_root / "source").mkdir(parents=True)
    (pdf_root / "source" / "main.tex").write_text("ignored", encoding="utf-8")
    (pdf_root / "paper.pdf").write_bytes(b"%PDF")
    write_yaml_file(pdf_root / "metadata.yaml", {"arxiv_id": "2301.12345", "primary_ingestion": "pdf", "pdf_available": True})

    metadata_root = tmp_path / "corpus" / "arxiv" / "2301.99999"
    metadata_root.mkdir(parents=True)
    (metadata_root / "paper.pdf").write_bytes(b"%PDF")
    write_yaml_file(metadata_root / "metadata.yaml", {"arxiv_id": "2301.99999", "primary_ingestion": "metadata"})

    files = discover_files(tmp_path / "corpus")

    assert pdf_root / "paper.pdf" in files
    assert pdf_root / "source" / "main.tex" not in files
    assert metadata_root / "paper.pdf" not in files


def test_download_records_pdf_fallback_and_metadata_only(tmp_path):
    pdf_candidate = _candidate("2301.22222", action="download")
    candidates_path = tmp_path / "pdf.yaml"
    write_candidates(candidates_path, [pdf_candidate])

    results = download_approved_papers(
        str(candidates_path),
        corpus_arxiv_dir=str(tmp_path / "arxiv"),
        client=FakeDownloadClient(fail_source=True),
    )

    assert results[0].source_downloaded is False
    assert results[0].pdf_downloaded is True
    metadata = load_yaml_file(tmp_path / "arxiv" / "2301.22222" / "metadata.yaml")
    assert metadata["primary_ingestion"] == "pdf"

    metadata_candidate = _candidate("2301.33333", action="download")
    metadata_path_only = tmp_path / "metadata.yaml"
    write_candidates(metadata_path_only, [metadata_candidate])
    results = download_approved_papers(
        str(metadata_path_only),
        corpus_arxiv_dir=str(tmp_path / "arxiv2"),
        client=FakeDownloadClient(fail_source=True, fail_pdf=True),
    )

    assert results[0].status == "metadata_only"
    metadata = load_yaml_file(tmp_path / "arxiv2" / "2301.33333" / "metadata.yaml")
    assert metadata["primary_ingestion"] == "metadata"


def test_non_ingestible_source_uses_pdf_fallback_and_preserves_ranking_reasons(tmp_path):
    candidate = _candidate("2301.44444", action="download")
    candidates_path = tmp_path / "candidate.yaml"
    write_candidates(candidates_path, [candidate])

    results = download_approved_papers(
        str(candidates_path),
        corpus_arxiv_dir=str(tmp_path / "arxiv"),
        client=FakeDownloadClient(source_bytes=_tar_bytes({"README": "no TeX here"})),
    )

    assert results[0].source_downloaded is True
    assert results[0].pdf_downloaded is True
    metadata = load_yaml_file(tmp_path / "arxiv" / "2301.44444" / "metadata.yaml")
    assert metadata["source_available"] is True
    assert metadata["primary_ingestion"] == "pdf"
    assert metadata["ranking_reasons"] == ["matched keyword: toric Kähler"]
    assert metadata["discovery_score"] == 0.5


def _candidate(arxiv_id, action="pending"):
    return PaperCandidate(
        arxiv_id=arxiv_id,
        version="v2",
        title="Candidate paper",
        authors=["Author A"],
        year=2023,
        arxiv_categories=["math.DG"],
        abstract="A paper about toric cscK metrics.",
        score=0.5,
        ranking_reasons=["matched keyword: toric Kähler"],
        action=action,
        source_url=f"https://arxiv.org/e-print/{arxiv_id}v2",
        pdf_url=f"https://arxiv.org/pdf/{arxiv_id}v2",
    )


def _tar_bytes(files):
    handle = io.BytesIO()
    with tarfile.open(fileobj=handle, mode="w:gz") as archive:
        for name, content in files.items():
            encoded = content.encode("utf-8")
            info = tarfile.TarInfo(name)
            info.size = len(encoded)
            archive.addfile(info, io.BytesIO(encoded))
    return handle.getvalue()
