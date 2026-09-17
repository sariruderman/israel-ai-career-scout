from dataclasses import dataclass

from app.acquisition.metadata import (
    extract_company,
    extract_location,
    extract_source,
)
from app.acquisition.models import ParsedDocument


@dataclass(frozen=True)
class NormalizedJob:
    title: str
    description: str
    url: str
    company: str
    location: str
    source: str


def normalize(document: ParsedDocument, source_url: str) -> NormalizedJob:
    return NormalizedJob(
        title=document.title,
        description=document.text,
        url=source_url,
        company=extract_company(document),
        location=extract_location(document),
        source=extract_source(source_url),
    )
