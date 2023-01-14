def format_complex(value):
    BOOL_TYPES = {'null', 'true', 'false', '0'}
    if isinstance(value, dict):
        return '[complex value]'
    elif value in BOOL_TYPES:
        return value
    else:
        return f"'{value}'"


def build_plain_string(status, path, value):
    if status == 'removed':
        return f"Property '{'.'.join(path)}' was removed" + '\n'
    elif status == 'added':
        return f"Property '{'.'.join(path)}' was added with value: "\
               f"{format_complex(value)}" + '\n'
    elif status == 'changed':
        return f"Property '{'.'.join(path)}' was updated. "\
               f"From {format_complex(value['old'])} to "\
               f"{format_complex(value['new'])}" + '\n'
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
