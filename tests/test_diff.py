import sys

from gendiff.cli import main
from gendiff.diff_builder import generate_diff


def test_json():
    result = generate_diff(
        "tests/test_data/file1.json",
        "tests/test_data/file2.json",
    )
    assert isinstance(result, str)


def test_yaml():
    result = generate_diff(
        "tests/test_data/file1.yml",
        "tests/test_data/file2.yml",
    )
    assert isinstance(result, str)


def test_plain_format():
    result = generate_diff(
        "tests/test_data/file1.json",
        "tests/test_data/file2.json",
        "plain",
    )

    assert isinstance(result, str)
    assert "Property" in result


def test_json_format():
    result = generate_diff(
        "tests/test_data/file1.json",
        "tests/test_data/file2.json",
        "json",
    )

    assert isinstance(result, str)
    assert "common" in result or "host" in result


def test_cli(capsys, monkeypatch):
    monkeypatch.setattr(
        sys,
        "argv",
        [
            "gendiff",
            "tests/test_data/file1.json",
            "tests/test_data/file2.json",
        ],
    )

    main()

    output = capsys.readouterr().out
    assert output