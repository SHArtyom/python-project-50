import json


def format_data(string):
    if isinstance(string, dict):
        return string
    output = json.dumps(string)
    output = output.replace('"', '')
    return output


def modify_keys(diff):
    diff_dict = {}
    for key in diff:
        if diff[key].get('status') == 'changed':
            diff_dict[f'- {key}'] = format_data(diff[key]['value']['old'])
            diff_dict[f'+ {key}'] = format_data(diff[key]['value']['new'])
        elif diff[key].get('status') == 'added':
            diff_dict[f'+ {key}'] = format_data(diff[key]['value'])
        elif diff[key].get('status') == 'removed':
            diff_dict[f'- {key}'] = format_data(diff[key]['value'])
        elif diff[key].get('status') == 'unchanged':
            diff_dict[f'{key}'] = format_data(diff[key]['value'])
        else:
            diff_dict[f'{key}'] = modify_keys(diff[key])
    return diff_dict


def stylish(diff):
    diff_dict = modify_keys(diff)

    def walk(value, depth=0):
        result = '{\n'
        if not isinstance(value, dict):
            return value
        for key in value:
            if '+' in str(key) or '-' in str(key):
                result += f"{' ' * (depth + 2)}{key}: "
            else:
                result += f"{' ' * (depth + 2)}  {key}: "
            if isinstance(value[key], dict):
                result += f'{walk(value[key], depth + 4)}\n'
            else:
                result += f'{value[key]}\n'
        return result + depth * ' ' + '}'
    return walk(diff_dict)
