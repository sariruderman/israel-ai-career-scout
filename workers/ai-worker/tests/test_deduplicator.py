from app.acquisition.deduplicator import canonicalize_url, is_duplicate
from app.acquisition.normalizer import NormalizedJob


def test_canonicalize_url_keeps_basic_url_unchanged():
    url = "https://example.com/jobs/123"

    assert canonicalize_url(url) == "https://example.com/jobs/123"


def test_canonicalize_url_removes_trailing_slash():
    url = "https://example.com/jobs/123/"

    assert canonicalize_url(url) == "https://example.com/jobs/123"


def test_canonicalize_url_removes_tracking_parameters():
    url = "https://example.com/jobs/123?utm_source=google&utm_campaign=test"

    assert canonicalize_url(url) == "https://example.com/jobs/123"


def test_canonicalize_url_keeps_meaningful_query_parameters():
    url = "https://example.com/jobs/123?lang=en&utm_source=google"

    assert canonicalize_url(url) == "https://example.com/jobs/123?lang=en"


def test_jobs_with_same_canonical_url_are_duplicates():
    first_job = NormalizedJob(
        title="Python Developer",
        description="Backend development position.",
        url="https://example.com/jobs/123",
    )

    second_job = NormalizedJob(
        title="Python Developer",
        description="Backend development position.",
        url="https://example.com/jobs/123?utm_source=google",
    )

    assert is_duplicate(first_job, second_job) is True


def test_jobs_with_different_urls_are_not_duplicates():
    first_job = NormalizedJob(
        title="Python Developer",
        description="Backend development position.",
        url="https://example.com/jobs/123",
    )

    second_job = NormalizedJob(
        title="Python Developer",
        description="Backend development position.",
        url="https://example.com/jobs/456",
    )

    assert is_duplicate(first_job, second_job) is False


def test_jobs_with_different_meaningful_query_parameters_are_not_duplicates():
    first_job = NormalizedJob(
        title="Python Developer",
        description="Backend development position.",
        url="https://example.com/jobs/123?lang=en",
    )

    second_job = NormalizedJob(
        title="Python Developer",
        description="Backend development position.",
        url="https://example.com/jobs/123?lang=fr",
    )

    assert is_duplicate(first_job, second_job) is False


def test_canonicalize_url_preserves_non_tracking_query_parameters():
    url = "https://example.com/jobs/123?lang=en&utm_source=google"

    assert canonicalize_url(url) == "https://example.com/jobs/123?lang=en"
