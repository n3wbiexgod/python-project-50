def format_value(value, depth):
    if isinstance(value, dict):
        indent = " " * (depth * 4)
        lines = ["{"]
        for k, v in value.items():
            lines.append(f"{indent}    {k}: {v}")
        lines.append(f"{indent}}}")
        return "\n".join(lines)
    return str(value)


def format_stylish(diff, depth=0):
    indent = " " * (depth * 4)
    lines = ["{"]

    for node in diff:
        key = node["key"]
        t = node["type"]

        if t == "nested":
            value = format_stylish(node["children"], depth + 1)
            lines.append(f"{indent}    {key}: {value}")

        elif t == "added":
            lines.append(f"{indent}  + {key}: {node['value']}")

        elif t == "removed":
            lines.append(f"{indent}  - {key}: {node['value']}")

        elif t == "unchanged":
            lines.append(f"{indent}    {key}: {node['value']}")

        elif t == "changed":
            lines.append(f"{indent}  - {key}: {node['old_value']}")
            lines.append(f"{indent}  + {key}: {node['new_value']}")

    lines.append(indent + "}")
    return "\n".join(lines)