from gendiff.formatters import format_diff
from gendiff.parsers import parse


def read_file(path):
    with open(path) as f:
        return f.read()


def get_format(path):
    return path.split(".")[-1]


def build_diff(data1, data2):
    keys = sorted(set(data1) | set(data2))
    result = []

    for key in keys:
        if key not in data1:
            result.append({
                "key": key,
                "type": "added",
                "value": data2[key]
            })

        elif key not in data2:
            result.append({
                "key": key,
                "type": "removed",
                "value": data1[key]
            })

        elif isinstance(data1[key], dict) and isinstance(data2[key], dict):
            result.append({
                "key": key,
                "type": "nested",
                "children": build_diff(data1[key], data2[key])
            })

        elif data1[key] == data2[key]:
            result.append({
                "key": key,
                "type": "unchanged",
                "value": data1[key]
            })

        else:
            result.append({
                "key": key,
                "type": "changed",
                "old_value": data1[key],
                "new_value": data2[key]
            })

    return result


def generate_diff(file1, file2, format_name="stylish"):
    data1 = parse(read_file(file1), get_format(file1))
    data2 = parse(read_file(file2), get_format(file2))

    diff = build_diff(data1, data2)

    return format_diff(diff, format_name)