import json

def read_file(path):
    with open(path) as f:
        return json.load(f)


def generate_diff(file1, file2):
    data1 = read_file(file1)
    data2 = read_file(file2)

    keys = sorted(set(data1) | set(data2))

    lines = ["{"]

    for key in keys:
        if key in data1 and key not in data2:
            lines.append(f"- {key}: {data1[key]}")
        elif key not in data1 and key in data2:
            lines.append(f"+ {key}: {data2[key]}")
        elif data1[key] == data2[key]:
            lines.append(f"  {key}: {data1[key]}")
        else:
            lines.append(f"- {key}: {data1[key]}")
            lines.append(f"+ {key}: {data2[key]}")

    lines.append("}")

    return "\n".join(lines)