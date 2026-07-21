import json
from pathlib import Path


REPORT_PATH = Path("/app/report.json")


def load_report():
    return json.loads(REPORT_PATH.read_text(encoding="utf-8"))


def test_report_path_format_and_schema():
    """Success criterion 1: the output path, JSON format, and exact schema."""
    assert REPORT_PATH.is_file(), "missing /app/report.json"
    report = load_report()
    assert isinstance(report, dict), "report must be a JSON object"
    assert set(report) == {"total_requests", "unique_ips", "top_path"}


def test_request_and_client_counts():
    """Success criterion 2: exact request and distinct-client counts."""
    report = load_report()
    assert type(report["total_requests"]) is int
    assert report["total_requests"] == 6
    assert type(report["unique_ips"]) is int
    assert report["unique_ips"] == 3


def test_top_path():
    """Success criterion 3: the most frequently requested path."""
    report = load_report()
    assert isinstance(report["top_path"], str)
    assert report["top_path"] == "/index.html"
