from bs4 import BeautifulSoup

from app.acquisition.models import ParsedDocument, ParsedLink


def parse_html(html: str) -> ParsedDocument:
    soup = BeautifulSoup(html, "html.parser")

    title = soup.title.get_text(strip=True) if soup.title else ""

    for element in soup(["script", "style", "noscript"]):
        element.decompose()

    text = soup.get_text(" ", strip=True)

    links = [
        ParsedLink(
            text=link.get_text(" ", strip=True),
            href=link.get("href"),
        )
        for link in soup.find_all("a", href=True)
    ]

    return ParsedDocument(
        title=title,
        text=text,
        links=links,
    )
