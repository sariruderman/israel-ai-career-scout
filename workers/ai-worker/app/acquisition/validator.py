from app.acquisition.normalizer import NormalizedJob


def validate_job(job: NormalizedJob) -> bool:
    return bool(job.title and job.description and job.url)
