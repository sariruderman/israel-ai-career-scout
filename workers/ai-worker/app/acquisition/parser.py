from bs4 import BeautifulSoup


def parse_html(html: str) -> dict:
    soup = BeautifulSoup(html, "html.parser")

    title = soup.title.get_text(strip=True) if soup.title else ""

    for element in soup(["script", "style", "noscript"]):
        element.decompose()

    text = soup.get_text(" ", strip=True)

    links = [
        {
            "text": link.get_text(" ", strip=True),
            "href": link.get("href"),
        }
        for link in soup.find_all("a", href=True)
    ]

    return {
        "title": title,
        "text": text,
        "links": links,
    }
