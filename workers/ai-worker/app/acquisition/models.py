from dataclasses import dataclass


@dataclass(frozen=True)
class ParsedLink:
    text: str
    href: str


@dataclass(frozen=True)
class ParsedDocument:
    title: str
    text: str
    links: list[ParsedLink]
