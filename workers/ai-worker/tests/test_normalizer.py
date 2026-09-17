from app.acquisition.models import ParsedDocument
from app.acquisition.normalizer import NormalizedJob, normalize


def test_normalized_job():
    job = NormalizedJob(
        title="Python Developer",
        description="Backend development position.",
        url="https://example.com/jobs/123",
    )

    assert job.title == "Python Developer"
    assert job.description == "Backend development position."
    assert job.url == "https://example.com/jobs/123"


def test_normalize_document():
    document = ParsedDocument(
        title="Python Developer",
        text="Backend development position.",
        links=[],
    )

    result = normalize(
        document,
        "https://example.com/jobs/123",
    )

    assert isinstance(result, NormalizedJob)
    assert result.title == "Python Developer"
    assert result.description == "Backend development position."
    assert result.url == "https://example.com/jobs/123"
