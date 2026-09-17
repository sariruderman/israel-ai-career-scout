from dataclasses import dataclass, field


@dataclass(frozen=True)
class ParsedLink:
    text: str
    href: str


@dataclass(frozen=True)
class ParsedDocument:
    title: str
    text: str
    links: list[ParsedLink]
    metadata: dict[str, str] = field(default_factory=dict)
