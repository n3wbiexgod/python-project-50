def format_value(value):
    if isinstance(value, dict):
        return "[complex value]"
    if isinstance(value, str):
        return f"'{value}'"
    if value is None:
        return "null"
    if value is True:
        return "true"
    if value is False:
        return "false"
    return str(value)


def format_plain(diff, path=""):
    lines = []

    for node in diff:
        key = node["key"]
        property_path = f"{path}.{key}" if path else key
        t = node["type"]

        if t == "nested":
            lines.extend(format_plain(node["children"], property_path))

        elif t == "added":
            value = format_value(node["value"])
            lines.append(
                f"Property '{property_path}' was added with value: {value}"
            )

        elif t == "removed":
            lines.append(
                f"Property '{property_path}' was removed"
            )

        elif t == "changed":
            old = format_value(node["old_value"])
            new = format_value(node["new_value"])
            lines.append(
                f"Property '{property_path}' was updated. From {old} to {new}"
            )

    return "\n".join(lines)