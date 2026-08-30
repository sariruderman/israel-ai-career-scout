from pathlib import Path

import requests


RAW_DATA_DIR = Path(__file__).resolve().parents[2] / "data" / "raw"


def fetch_url(url: str) -> requests.Response:
    response = requests.get(
        url,
        timeout=20,
        headers={
            "User-Agent": "israel-ai-career-scout/0.1"
        },
    )

    response.raise_for_status()

    return response