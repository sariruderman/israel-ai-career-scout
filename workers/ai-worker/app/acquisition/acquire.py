from pathlib import Path

from app.acquisition.fetcher import fetch_url
from app.acquisition.storage import save_raw_snapshot


def acquire_url(url: str, output_path: Path) -> Path:
    response = fetch_url(url)

    return save_raw_snapshot(
        response.content,
        output_path,
    )
