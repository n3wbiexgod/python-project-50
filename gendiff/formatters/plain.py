def format_value(value):
    if isinstance(value, dict):
        return "[complex value]"
    if isinstance(value, str):
        return f"'{value}'"
    if value is True:
        return "true"
    if value is False:
        return "false"
    if value is None:
        return "null"
    return str(value)


def format_plain(diff, path=""):
    lines = []

    for node in diff:
        key = node["key"]
        full_path = f"{path}.{key}" if path else key
        t = node["type"]

        if t == "nested":
            lines.append(format_plain(node["children"], full_path))

        elif t == "added":
            lines.append(
                f"Property '{full_path}' was added with value: {format_value(node['value'])}"
            )

        elif t == "removed":
            lines.append(
                f"Property '{full_path}' was removed"
            )

        elif t == "changed":
            lines.append(
                f"Property '{full_path}' was updated. From {format_value(node['old_value'])} to {format_value(node['new_value'])}"
            )

    return "\n".join(filter(None, lines))