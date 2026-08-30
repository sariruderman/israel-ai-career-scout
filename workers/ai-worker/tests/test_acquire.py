from pathlib import Path
from unittest.mock import Mock, patch

from app.acquisition.acquire import acquire_url

@patch("app.acquisition.acquire.fetch_url")
def test_acquire_url_fetches_and_saves(mock_fetch_url, tmp_path: Path):
    fake_response = Mock()
    fake_response.content = b"test job content"

    
    mock_fetch_url.return_value = fake_response
    
    output_path = tmp_path / "raw" / "job_001.html"
    
    result = acquire_url(
        "https://example.com/job/001",
        output_path,
    )
    
    mock_fetch_url.assert_called_once_with(
        "https://example.com/job/001"
    )
    
    assert result == output_path
    assert output_path.exists()
    assert output_path.read_bytes() == b"test job content"

