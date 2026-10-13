from urllib.parse import urlparse

from app.acquisition.models import ParsedDocument


def extract_source(url: str) -> str:
    hostname = urlparse(url).hostname
    if not hostname:
        raise ValueError("URL must include a hostname")

    return hostname.lower().removeprefix("www.")


def extract_company(document: ParsedDocument) -> str:
    return document.metadata.get("company", "")


def extract_location(document: ParsedDocument) -> str:
    return document.metadata.get("location", "")
