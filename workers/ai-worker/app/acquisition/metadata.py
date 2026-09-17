from urllib.parse import urlparse

from app.acquisition.models import ParsedDocument


def extract_source(url: str) -> str:
    return urlparse(url).netloc.removeprefix("www.")


def extract_company(document: ParsedDocument) -> str:
    return document.metadata.get("company", "")


def extract_location(document: ParsedDocument) -> str:
    return document.metadata.get("location", "")
