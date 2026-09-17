from dataclasses import dataclass

from app.acquisition.models import ParsedDocument


@dataclass(frozen=True)
class NormalizedJob:
    title: str
    description: str
    url: str


def normalize(document: ParsedDocument, source_url: str) -> NormalizedJob:
    return NormalizedJob(
        title=document.title,
        description=document.text,
        url=source_url,
    )
