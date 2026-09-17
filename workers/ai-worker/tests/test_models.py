from app.acquisition.models import ParsedDocument, ParsedLink


def test_parsed_link():
    link = ParsedLink(
        text="View job",
        href="https://example.com/jobs/123",
    )

    assert link.text == "View job"
    assert link.href == "https://example.com/jobs/123"


def test_parsed_document():
    link = ParsedLink(
        text="View job",
        href="https://example.com/jobs/123",
    )

    document = ParsedDocument(
        title="Python Developer",
        text="Backend development position.",
        links=[link],
        metadata={},
    )

    assert document.title == "Python Developer"
    assert document.text == "Backend development position."
    assert document.links == [link]
    assert document.metadata == {}
