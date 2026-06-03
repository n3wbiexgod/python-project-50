def stringify(value, depth):
    indent = "    " * depth

    if isinstance(value, dict):
        lines = ["{"]
        for k, v in value.items():
            lines.append(f"{indent}    {k}: {stringify(v, depth + 1)}")
        lines.append(f"{indent}}}")
        return "\n".join(lines)

    if value is True:
        return "true"
    if value is False:
        return "false"
    if value is None:
        return "null"

    return str(value)


def format_stylish(diff, depth=0):
    indent = "    " * depth
    lines = ["{"]

    for node in diff:
        key = node["key"]
        t = node["type"]

        if t == "nested":
            value = format_stylish(node["children"], depth + 1)
            lines.append(f"{indent}    {key}: {value}")

        elif t == "added":
            value = stringify(node["value"], depth + 1)
            lines.append(f"{indent}  + {key}: {value}")

        elif t == "removed":
            value = stringify(node["value"], depth + 1)
            lines.append(f"{indent}  - {key}: {value}")

        elif t == "unchanged":
            value = stringify(node["value"], depth + 1)
            lines.append(f"{indent}    {key}: {value}")

        elif t == "changed":
            old = stringify(node["old_value"], depth + 1)
            new = stringify(node["new_value"], depth + 1)

            lines.append(f"{indent}  - {key}: {old}")
            lines.append(f"{indent}  + {key}: {new}")

    lines.append(indent + "}")
    return "\n".join(lines)