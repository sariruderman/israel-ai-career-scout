from dataclasses import dataclass


@dataclass(frozen=True)
class NormalizedJob:
    title: str
    description: str
    url: str
