from app.acquisition.metadata import (
    extract_company,
    extract_location,
    extract_source,
)
from app.acquisition.models import ParsedDocument


def test_extract_source_removes_www_prefix():
    url = "https://www.example.com/jobs/123"

    assert extract_source(url) == "example.com"


def test_extract_source_preserves_subdomain():
    url = "https://jobs.example.com/123"

    assert extract_source(url) == "jobs.example.com"


def test_extract_source_handles_url_without_path():
    url = "https://example.com"

    assert extract_source(url) == "example.com"


def test_extract_company_from_metadata():
    document = ParsedDocument(
        title="Python Developer",
        text="Backend development position.",
        links=[],
        metadata={
            "company": "Example Ltd",
        },
    )

    assert extract_company(document) == "Example Ltd"


def test_extract_location_from_metadata():
    document = ParsedDocument(
        title="Python Developer",
        text="Backend development position.",
        links=[],
        metadata={
            "location": "Tel Aviv",
        },
    )

    assert extract_location(document) == "Tel Aviv"
