import io
import tarfile
import urllib.error
from email.message import Message

from math_rag import cli as cli_module
from math_rag.arxiv_client import ArxivClient, ArxivPaper, parse_arxiv_atom, parse_arxiv_id, split_arxiv_id
from math_rag.downloader import download_arxiv_ids, download_seed_file, read_seed_arxiv_ids
from math_rag.loaders import load_corpus
from math_rag.paper_store import DownloadResult, load_yaml_file, safe_arxiv_dirname, write_yaml_file


class FakeArxivClient:
    def __init__(
        self,
        papers,
        source_bytes=None,
        pdf_bytes=b"%PDF fake",
        fail_source_ids=None,
        fail_pdf_ids=None,
    ):
        self.papers = papers
        self.source_bytes = source_bytes if source_bytes is not None else _tar_bytes({"main.tex": "\\section{A}\nText"})
        self.pdf_bytes = pdf_bytes
        self.fail_source_ids = set(fail_source_ids or [])
        self.fail_pdf_ids = set(fail_pdf_ids or [])
        self.fetch_requests = []
        self.download_urls = []

    def fetch_by_ids(self, identifiers):
        self.fetch_requests.append(list(identifiers))
        results = []
        for identifier in identifiers:
            parsed = parse_arxiv_id(identifier)
            for paper in self.papers:
                if paper.arxiv_id != parsed.arxiv_id:
                    continue
                if parsed.version and paper.version != parsed.version:
                    continue
                results.append(paper)
                break
        return results

    def download_bytes(self, url):
        self.download_urls.append(url)
        if "e-print" in url:
            if any(identifier in url for identifier in self.fail_source_ids):
                raise RuntimeError("no source")
            return self.source_bytes
        if any(identifier in url for identifier in self.fail_pdf_ids):
            raise RuntimeError("no pdf")
        return self.pdf_bytes


class BatchFailingFakeArxivClient(FakeArxivClient):
    def fetch_by_ids(self, identifiers):
        self.fetch_requests.append(list(identifiers))
        if len(identifiers) > 1:
            raise RuntimeError("batch metadata failure")
        return super().fetch_by_ids(identifiers)


def test_single_arxiv_id_download_and_ingest_prefers_tex(tmp_path):
    corpus_arxiv = tmp_path / "corpus" / "arxiv"
    client = FakeArxivClient([_paper("1711.08424v2")])

    results = download_arxiv_ids(["1711.08424v2"], corpus_arxiv_dir=str(corpus_arxiv), client=client)

    assert [result.status for result in results] == ["downloaded"]
    root = corpus_arxiv / "1711.08424"
    assert (root / "source" / "main.tex").exists()
    assert (root / "paper.pdf").exists()
    metadata = load_yaml_file(root / "metadata.yaml")
    assert metadata["arxiv_id"] == "1711.08424"
    assert metadata["version"] == "v2"
    assert metadata["requested_arxiv_id"] == "1711.08424v2"
    assert metadata["source_available"] is True
    assert metadata["pdf_available"] is True
    assert metadata["primary_ingestion"] == "tex"

    chunks, warnings = load_corpus(tmp_path / "corpus")
    assert warnings == []
    assert chunks
    assert chunks[0].metadata["arxiv_id"] == "1711.08424"
    assert chunks[0].metadata["ingestion_source"] == "tex"
    assert chunks[0].metadata["source_available"] is True
    assert chunks[0].metadata["pdf_available"] is True


def test_multiple_arxiv_ids_downloaded_in_order(tmp_path):
    client = FakeArxivClient([_paper("1711.08424"), _paper("math/0407486")])

    results = download_arxiv_ids(["1711.08424", "math/0407486"], corpus_arxiv_dir=str(tmp_path), client=client)

    assert [result.arxiv_id for result in results] == ["1711.08424", "math/0407486"]
    assert client.fetch_requests == [["1711.08424", "math/0407486"]]
    assert (tmp_path / "1711.08424" / "metadata.yaml").exists()
    assert (tmp_path / "math_0407486" / "metadata.yaml").exists()


def test_seed_file_download_uses_unique_non_comment_ids(tmp_path):
    seed = tmp_path / "arxiv_seed_core.txt"
    seed.write_text(
        "\n".join(
            [
                "# curated core list",
                "1711.08424",
                "1711.08424  # duplicate",
                "",
                "dg-ga/9711014",
            ]
        ),
        encoding="utf-8",
    )
    client = FakeArxivClient([_paper("1711.08424"), _paper("dg-ga/9711014")])

    assert read_seed_arxiv_ids(seed) == ["1711.08424", "1711.08424", "dg-ga/9711014"]
    results = download_seed_file(seed, corpus_arxiv_dir=str(tmp_path / "arxiv"), client=client)

    assert [result.arxiv_id for result in results] == ["1711.08424", "dg-ga/9711014"]
    assert client.fetch_requests == [["1711.08424", "dg-ga/9711014"]]


def test_old_style_ids_and_safe_path_generation(tmp_path):
    assert split_arxiv_id("math/0407486") == ("math/0407486", None)
    assert split_arxiv_id("dg-ga/9711014v1") == ("dg-ga/9711014", "v1")
    assert parse_arxiv_id("https://arxiv.org/pdf/math/0407486.pdf").arxiv_id == "math/0407486"
    assert safe_arxiv_dirname("math/0407486") == "math_0407486"
    assert safe_arxiv_dirname("dg-ga/9711014") == "dg-ga_9711014"
    assert safe_arxiv_dirname("..") == "unknown"

    client = FakeArxivClient([_paper("math/0407486"), _paper("dg-ga/9711014")])
    results = download_arxiv_ids(["math/0407486", "dg-ga/9711014"], corpus_arxiv_dir=str(tmp_path), client=client)

    assert [result.status for result in results] == ["downloaded", "downloaded"]
    assert (tmp_path / "math_0407486").exists()
    assert (tmp_path / "dg-ga_9711014").exists()


def test_old_style_atom_metadata_preserves_archive_prefix():
    atom = """<?xml version="1.0" encoding="UTF-8"?>
<feed xmlns="http://www.w3.org/2005/Atom">
  <entry>
    <id>http://arxiv.org/abs/math/0407486v1</id>
    <updated>2004-07-23T00:00:00Z</updated>
    <published>2004-07-23T00:00:00Z</published>
    <title>Old style paper</title>
    <summary>Summary.</summary>
    <author><name>Author A</name></author>
    <category term="math.DG" />
    <link title="pdf" href="https://arxiv.org/pdf/math/0407486v1" rel="related" type="application/pdf"/>
  </entry>
</feed>
"""

    paper = parse_arxiv_atom(atom)[0]

    assert paper.arxiv_id == "math/0407486"
    assert paper.version == "v1"
    assert paper.source_url.endswith("/math/0407486v1")
    assert paper.pdf_url.endswith("/math/0407486v1")


def test_download_limit_reports_skipped_seed_ids(tmp_path):
    client = FakeArxivClient([_paper("1711.08424"), _paper("math/0407486")])

    results = download_arxiv_ids(
        ["1711.08424", "math/0407486"],
        corpus_arxiv_dir=str(tmp_path),
        client=client,
        limit=1,
    )

    assert [result.status for result in results] == ["downloaded", "skipped_limit"]
    assert client.fetch_requests == [["1711.08424"]]


def test_metadata_batch_failure_falls_back_to_per_id_lookup(tmp_path):
    client = BatchFailingFakeArxivClient([_paper("1711.08424"), _paper("math/0407486")])

    results = download_arxiv_ids(["1711.08424", "math/0407486"], corpus_arxiv_dir=str(tmp_path), client=client)

    assert [result.status for result in results] == ["downloaded", "downloaded"]
    assert client.fetch_requests[0] == ["1711.08424", "math/0407486"]
    assert ["1711.08424"] in client.fetch_requests
    assert ["math/0407486"] in client.fetch_requests


def test_duplicate_detection_skips_exact_existing_version_without_network(tmp_path):
    root = tmp_path / "1711.08424"
    root.mkdir()
    write_yaml_file(root / "metadata.yaml", {"arxiv_id": "1711.08424", "version": "v2"})
    client = FakeArxivClient([])

    results = download_arxiv_ids(["1711.08424v2"], corpus_arxiv_dir=str(tmp_path), client=client)

    assert results[0].status == "skipped_duplicate"
    assert results[0].duplicate is True
    assert client.fetch_requests == []
    assert client.download_urls == []


def test_skip_existing_folder_without_metadata_avoids_network(tmp_path):
    root = tmp_path / "1711.08424"
    root.mkdir()
    (root / "note.txt").write_text("keep", encoding="utf-8")
    client = FakeArxivClient([_paper("1711.08424")])

    results = download_arxiv_ids(["1711.08424"], corpus_arxiv_dir=str(tmp_path), client=client, skip_existing=True)

    assert results[0].status == "skipped_existing_folder"
    assert (root / "note.txt").exists()
    assert client.fetch_requests == []
    assert client.download_urls == []


def test_force_replaces_existing_folder(tmp_path):
    root = tmp_path / "1711.08424"
    root.mkdir()
    (root / "old.txt").write_text("old", encoding="utf-8")
    client = FakeArxivClient([_paper("1711.08424")])

    results = download_arxiv_ids(["1711.08424"], corpus_arxiv_dir=str(tmp_path), client=client, force=True)

    assert results[0].status == "downloaded"
    assert not (root / "old.txt").exists()
    assert (root / "metadata.yaml").exists()
    assert (root / "source" / "main.tex").exists()


def test_source_pdf_fallback_and_metadata_only(tmp_path):
    pdf_client = FakeArxivClient([_paper("1711.08424")], fail_source_ids={"1711.08424"})

    pdf_results = download_arxiv_ids(["1711.08424"], corpus_arxiv_dir=str(tmp_path / "pdf"), client=pdf_client)

    assert pdf_results[0].source_downloaded is False
    assert pdf_results[0].pdf_downloaded is True
    metadata = load_yaml_file(tmp_path / "pdf" / "1711.08424" / "metadata.yaml")
    assert metadata["primary_ingestion"] == "pdf"
    assert metadata["download_errors"]

    metadata_client = FakeArxivClient(
        [_paper("1711.08424")],
        fail_source_ids={"1711.08424"},
        fail_pdf_ids={"1711.08424"},
    )
    metadata_results = download_arxiv_ids(
        ["1711.08424"],
        corpus_arxiv_dir=str(tmp_path / "metadata"),
        client=metadata_client,
    )

    assert metadata_results[0].status == "metadata_only"
    metadata = load_yaml_file(tmp_path / "metadata" / "1711.08424" / "metadata.yaml")
    assert metadata["primary_ingestion"] == "metadata"


def test_text_only_source_bundle_uses_pdf_fallback(tmp_path):
    client = FakeArxivClient([_paper("1711.08424")], source_bytes=_tar_bytes({"README.txt": "not the paper"}))

    results = download_arxiv_ids(["1711.08424"], corpus_arxiv_dir=str(tmp_path), client=client)

    assert results[0].status == "downloaded"
    metadata = load_yaml_file(tmp_path / "1711.08424" / "metadata.yaml")
    assert metadata["source_available"] is True
    assert metadata["pdf_available"] is True
    assert metadata["primary_ingestion"] == "pdf"


def test_arxiv_client_retries_429_once(monkeypatch):
    sleeps = []
    calls = {"count": 0}

    class FakeResponse:
        def __enter__(self):
            return self

        def __exit__(self, exc_type, exc, traceback):
            return False

        def read(self):
            return b"ok"

    def fake_urlopen(request, timeout):
        calls["count"] += 1
        if calls["count"] == 1:
            headers = Message()
            headers["Retry-After"] = "2"
            raise urllib.error.HTTPError(request.full_url, 429, "Too Many Requests", headers, None)
        return FakeResponse()

    monkeypatch.setattr("urllib.request.urlopen", fake_urlopen)
    monkeypatch.setattr("time.sleep", lambda seconds: sleeps.append(seconds))

    client = ArxivClient(delay_seconds=0, max_429_retries=1)

    assert client.download_bytes("https://arxiv.org/pdf/1711.08424") == b"ok"
    assert calls["count"] == 2
    assert sleeps == [2.0]


def test_cli_force_and_skip_existing_flags(monkeypatch):
    calls = []

    def fake_download(arxiv_ids, corpus_arxiv_dir, config_path, limit, force, skip_existing):
        calls.append(
            {
                "ids": arxiv_ids,
                "corpus": corpus_arxiv_dir,
                "config": config_path,
                "limit": limit,
                "force": force,
                "skip_existing": skip_existing,
            }
        )
        return [DownloadResult(arxiv_id=arxiv_ids[0], version=None, status="skipped_existing_folder")]

    monkeypatch.setattr(cli_module, "download_arxiv_ids", fake_download)

    assert cli_module._argparse_main(["download-arxiv", "1711.08424", "--force"]) == 0
    assert calls[-1]["force"] is True
    assert calls[-1]["skip_existing"] is False

    assert cli_module._argparse_main(["download-arxiv", "1711.08424", "--skip-existing"]) == 0
    assert calls[-1]["force"] is False
    assert calls[-1]["skip_existing"] is True


def _paper(identifier):
    parsed = parse_arxiv_id(identifier)
    version = parsed.version or "v1"
    id_with_version = f"{parsed.arxiv_id}{version}"
    return ArxivPaper(
        arxiv_id=parsed.arxiv_id,
        version=version,
        title=f"Paper {parsed.arxiv_id}",
        authors=["Author A"],
        abstract="A paper about toric cscK metrics.",
        year=2024,
        categories=["math.DG"],
        source_url=f"https://arxiv.org/e-print/{id_with_version}",
        pdf_url=f"https://arxiv.org/pdf/{id_with_version}",
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
