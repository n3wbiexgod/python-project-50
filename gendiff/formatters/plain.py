def stringify(value):
    if isinstance(value, dict):
        return "[complex value]"

    if value is True:
        return "true"
    if value is False:
        return "false"
    if value is None:
        return "null"

    if isinstance(value, str):
        return f"'{value}'"

    return str(value)


def format_plain(diff, path=""):
    lines = []

    for node in diff:
        key = node["key"]
        type_ = node["type"]

        full_path = f"{path}.{key}" if path else key

        if type_ == "nested":
            lines.append(format_plain(node["children"], full_path))

        elif type_ == "added":
            value = stringify(node["value"])
            lines.append(
                f"Property '{full_path}' was added with value: {value}"
            )

        elif type_ == "removed":
            lines.append(
                f"Property '{full_path}' was removed"
            )

        elif type_ == "changed":
            old = stringify(node["old_value"])
            new = stringify(node["new_value"])
            lines.append(
                f"Property '{full_path}' was updated. From {old} to {new}"
            )

    return "\n".join(lines)