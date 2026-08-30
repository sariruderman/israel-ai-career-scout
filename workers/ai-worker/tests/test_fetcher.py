from unittest.mock import patch

import pytest
import requests

from app.acquisition.fetcher import fetch_url


@patch("app.acquisition.fetcher.requests.get")
def test_fetch_url_returns_successful_response(mock_get):
    mock_response = mock_get.return_value
    mock_response.status_code = 200

    response = fetch_url("https://example.com")

    assert response.status_code == 200


@patch("app.acquisition.fetcher.requests.get")
def test_fetch_url_uses_expected_request_settings(mock_get):
    mock_response = mock_get.return_value
    mock_response.status_code = 200

    fetch_url("https://example.com")

    mock_get.assert_called_once_with(
        "https://example.com",
        timeout=20,
        headers={
            "User-Agent": "israel-ai-career-scout/0.1"
        },
    )


@patch("app.acquisition.fetcher.requests.get")
def test_fetch_url_calls_raise_for_status(mock_get):
    mock_response = mock_get.return_value
    mock_response.status_code = 200

    fetch_url("https://example.com")

    mock_response.raise_for_status.assert_called_once()


@patch("app.acquisition.fetcher.requests.get")
def test_fetch_url_raises_http_error(mock_get):
    mock_response = mock_get.return_value
    mock_response.status_code = 404

    mock_response.raise_for_status.side_effect = requests.HTTPError(
        "404 Client Error"
    )

    with pytest.raises(requests.HTTPError):
        fetch_url("https://example.com")