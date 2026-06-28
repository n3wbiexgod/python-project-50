import subprocess
import sys
from gendiff.diff_builder import generate_diff


def test_json():
    result = generate_diff(
        "tests/test_data/file1.json",
        "tests/test_data/file2.json",
    )
    assert result is not None
    assert isinstance(result, str)
    assert len(result) > 0


def test_yaml():
    result = generate_diff(
        "tests/test_data/file1.yml",
        "tests/test_data/file2.yml",
    )
    assert result is not None
    assert isinstance(result, str)
    assert len(result) > 0


def test_plain_format():
    result = generate_diff(
        "tests/test_data/file1.json",
        "tests/test_data/file2.json",
        "plain",
    )

    assert "Property" in result
    assert isinstance(result, str)


def test_json_format():
    result = generate_diff(
        "tests/test_data/file1.json",
        "tests/test_data/file2.json",
        "json",
    )

    assert "{" in result or "common" in result


def test_cli():
    result = subprocess.run(
        [
            sys.executable,
            "-m",
            "gendiff",
            "tests/test_data/file1.json",
            "tests/test_data/file2.json",
        ],
        capture_output=True,
        text=True,
    )

    assert result.returncode == 0
    assert len(result.stdout) > 0