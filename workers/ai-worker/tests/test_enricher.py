from app.acquisition.enricher import EnrichedJob, enrich
from app.acquisition.normalizer import NormalizedJob


def test_enriched_job_contains_basic_metadata():
    job = EnrichedJob(
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


def test_enrich_adds_metadata_to_normalized_job():

    job = NormalizedJob(
        title="Python Developer",
        description="Backend development position.",
        url="https://example.com/jobs/123",
    )

    result = enrich(
        job,
        company="Example Ltd",
        location="Tel Aviv",
        source="example.com",
    )

    assert isinstance(result, EnrichedJob)
    assert result.company == "Example Ltd"
    assert result.location == "Tel Aviv"
    assert result.source == "example.com"
