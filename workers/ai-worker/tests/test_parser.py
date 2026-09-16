from app.acquisition.models import ParsedDocument, ParsedLink
from app.acquisition.parser import parse_html


def test_parse_html_extracts_title_text_and_links():
    html = """
    <html>
        <head>
            <title>Python Developer</title>
            <style>.hidden { display: none; }</style>
        </head>
        <body>
            <h1>Python Developer</h1>
            <p>Backend development position.</p>
            <a href="https://example.com/jobs/123">View job</a>
            <script>
                console.log("should not appear");
            </script>
        </body>
    </html>
    """

    result = parse_html(html)

    assert isinstance(result, ParsedDocument)
    assert result.title == "Python Developer"
    assert "Backend development position." in result.text
    assert "should not appear" not in result.text
    assert result.links == [
        ParsedLink(
            text="View job",
            href="https://example.com/jobs/123",
        )
    ]


def test_parse_html_handles_missing_title():
    html = """
    <html>
        <body>
            <p>Some content</p>
        </body>
    </html>
    """

    result = parse_html(html)

    assert isinstance(result, ParsedDocument)
    assert result.title == ""
    assert "Some content" in result.text
    assert result.links == []


def test_parse_html_ignores_links_without_href():
    html = """
    <html>
        <body>
            <a>Not a real link</a>
            <a href="/jobs/1">Job 1</a>
        </body>
    </html>
    """

    result = parse_html(html)

    assert result.links == [
        ParsedLink(
            text="Job 1",
            href="/jobs/1",
        )
    ]
