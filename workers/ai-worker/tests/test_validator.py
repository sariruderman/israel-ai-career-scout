from app.acquisition.normalizer import NormalizedJob
from app.acquisition.validator import validate_job


def test_valid_job():
    job = NormalizedJob(
        title="Python Developer",
        description="Backend development position.",
        url="https://example.com/jobs/123",
    )

    assert validate_job(job) is True


def test_job_with_empty_title_is_invalid():
    job = NormalizedJob(
        title="",
        description="Backend development position.",
        url="https://example.com/jobs/123",
    )

    assert validate_job(job) is False


def test_job_with_empty_description_is_invalid():
    job = NormalizedJob(
        title="Python Developer",
        description="",
        url="https://example.com/jobs/123",
    )

    assert validate_job(job) is False


def test_job_with_empty_url_is_invalid():
    job = NormalizedJob(
        title="Python Developer",
        description="Backend development position.",
        url="",
    )

    assert validate_job(job) is False
