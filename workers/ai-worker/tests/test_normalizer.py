from app.acquisition.models import ParsedDocument
from app.acquisition.normalizer import NormalizedJob, normalize


def test_normalized_job():
    job = NormalizedJob(
        title="Python Developer",
        description="Backend development position.",
        url="https://example.com/jobs/123",
        company="Example Ltd",
        location="Tel Aviv",
        source="example.com",
    )

    assert job.title == "Python Developer"
    assert job.description == "Backend development position."
    assert job.url == "https://example.com/jobs/123"
    assert job.company == "Example Ltd"
    assert job.location == "Tel Aviv"
    assert job.source == "example.com"


def test_normalize_document():
    document = ParsedDocument(
        title="Python Developer",
        text="Backend development position.",
        links=[],
        metadata={
            "company": "Example Ltd",
            "location": "Tel Aviv",
        },
    )

    result = normalize(
        document,
        "https://www.example.com/jobs/123",
    )

    assert isinstance(result, NormalizedJob)
    assert result.title == "Python Developer"
    assert result.description == "Backend development position."
    assert result.url == "https://www.example.com/jobs/123"
    assert result.company == "Example Ltd"
    assert result.location == "Tel Aviv"
    assert result.source == "example.com"
