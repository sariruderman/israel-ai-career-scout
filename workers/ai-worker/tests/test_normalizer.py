from app.acquisition.normalizer import NormalizedJob


def test_normalized_job():
    job = NormalizedJob(
        title="Python Developer",
        description="Backend development position.",
        url="https://example.com/jobs/123",
    )

    assert job.title == "Python Developer"
    assert job.description == "Backend development position."
    assert job.url == "https://example.com/jobs/123"
