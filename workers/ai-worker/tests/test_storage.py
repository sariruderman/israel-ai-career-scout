from pathlib import Path

from app.acquisition.storage import save_raw_snapshot


def test_save_raw_snapshot(tmp_path: Path):
    content = b"test job content"
    output_path = tmp_path / "raw" / "job_001.html"

    result = save_raw_snapshot(content, output_path)

    assert result == output_path
    assert output_path.exists()
    assert output_path.read_bytes() == content


def test_save_raw_snapshot_empty_content(tmp_path: Path):
    content = b""
    output_path = tmp_path / "raw" / "empty.html"

    result = save_raw_snapshot(content, output_path)

    assert result == output_path
    assert output_path.exists()
    assert output_path.read_bytes() == b""
