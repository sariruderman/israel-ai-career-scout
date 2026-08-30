from pathlib import Path

from app.acquisition.acquire import acquire_url


def main() -> None:
    url = "https://example.com"

    output_path = Path("data/raw/example.html")

    saved_path = acquire_url(
        url,
        output_path,
    )

    print(f"Raw snapshot saved to: {saved_path}")


if __name__ == "__main__":
    main()