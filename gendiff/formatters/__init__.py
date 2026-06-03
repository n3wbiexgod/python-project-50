from gendiff.formatters.stylish import format_stylish
from gendiff.formatters.plain import format_plain
from gendiff.formatters.json import format_json


def format_diff(diff, format_name="stylish"):
    if format_name == "plain":
        return format_plain(diff)

    if format_name == "json":
        return format_json(diff)

    return format_stylish(diff)