def format_complex(value):
    if isinstance(value, dict):
        return '[complex value]'
    else:
        return f"'{value}'"


def plain(diff):
    def walk(diff, path, result):
        for key in diff:
            path.append(key)
            if diff[key].get('status') == 'removed':
                result += f"Property '{'.'.join(path)}' was removed" + '\n'
            elif diff[key].get('status') == 'added':
                result += f"Property '{'.'.join(path)}' was added with value: " \
                          f"{format_complex(diff[key]['value'])}" + '\n'
            elif diff[key].get('status') == 'changed':
                result += f"Property '{'.'.join(path)}' was updated. From " \
                          f"{format_complex(diff[key]['value']['old'])} to " \
                          f"{format_complex(diff[key]['value']['new'])}" + '\n'
            elif diff[key].get('status') == 'unchanged':
                path.pop()
                continue
            else:
                result = walk(diff[key], path, result)
            path.pop()
        return result
    return walk(diff, [], '')
