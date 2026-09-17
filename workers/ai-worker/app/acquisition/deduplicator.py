from urllib.parse import parse_qsl, urlencode, urlparse, urlunparse

from app.acquisition.normalizer import NormalizedJob

TRACKING_PARAMETERS = {
    "utm_source",
    "utm_medium",
    "utm_campaign",
    "utm_term",
    "utm_content",
}


def canonicalize_url(url: str) -> str:
    parsed = urlparse(url)

    query_parameters = [
        (key, value)
        for key, value in parse_qsl(parsed.query, keep_blank_values=True)
        if key not in TRACKING_PARAMETERS
    ]

    path = parsed.path.rstrip("/") or "/"

    return urlunparse(
        (
            parsed.scheme,
            parsed.netloc,
            path,
            parsed.params,
            urlencode(query_parameters),
            "",
        )
    )


def is_duplicate(first_job: NormalizedJob, second_job: NormalizedJob) -> bool:
    return canonicalize_url(first_job.url) == canonicalize_url(second_job.url)
