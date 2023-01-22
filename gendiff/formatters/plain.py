def to_str(value):
    if isinstance(value, dict):
        return '[complex value]'
    elif isinstance(value, bool):
        return str(value).lower()
    elif value is None:
        return 'null'
    else:
        return f"'{value}'"


def build_plain_string(status, path, value):
    if status == 'removed':
        return f"Property '{'.'.join(path)}' was removed" + '\n'
    elif status == 'added':
        return f"Property '{'.'.join(path)}' was added with value: "\
               f"{to_str(value)}" + '\n'
    elif status == 'changed':
        return f"Property '{'.'.join(path)}' was updated. "\
               f"From {to_str(value['old'])} "\
               f"to {to_str(value['new'])}" + '\n'
    else:
        return ''


def plain(diff):
    def walk(diff, path, result):
        for key in diff:
            path.append(key)
            if not diff[key].get('status'):
                result = walk(diff[key], path, result)
            else:
                status = diff[key].get('status')
                value = diff[key]['value']
                result += str(build_plain_string(status, path, value))
            path.pop()
        return result
    return walk(diff, [], '').rstrip('\n')
