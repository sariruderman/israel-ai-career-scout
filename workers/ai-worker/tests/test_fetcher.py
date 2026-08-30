from unittest.mock import patch

from app.acquisition.fetcher import fetch_url


@patch("app.acquisition.fetcher.requests.get")
def test_fetch_url_returns_successful_response(mock_get):
    mock_response = mock_get.return_value
    mock_response.status_code = 200

    response = fetch_url("https://example.com")

    assert response.status_code == 200
    mock_get.assert_called_once()