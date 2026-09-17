from dataclasses import dataclass

from app.acquisition.normalizer import NormalizedJob


@dataclass(frozen=True)
class EnrichedJob:
    title: str
    description: str
    url: str
    company: str
    location: str
    source: str


def enrich(
    job: NormalizedJob,
    company: str,
    location: str,
    source: str,
) -> EnrichedJob:
    return EnrichedJob(
        title=job.title,
        description=job.description,
        url=job.url,
        company=company,
        location=location,
        source=source,
    )
