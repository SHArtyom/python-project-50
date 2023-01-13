import json
import yaml
from yaml import SafeLoader
from gendiff.formatters.stylish import stylish


def get_data(file_path1, file_path2):
    if '.json' in file_path1[-6:]:
        with open(file_path1, 'r') as f1:
            file1 = json.load(f1)
        with open(file_path2, 'r') as f2:
            file2 = json.load(f2)
    elif '.yaml' or '.yml' in file_path1[-6:]:
        with open(file_path1, 'r') as f1:
            file1 = yaml.load(f1, Loader=SafeLoader)
        with open(file_path2, 'r') as f2:
            file2 = yaml.load(f2, Loader=SafeLoader)
    return file1, file2


def format_data(string):
    if isinstance(string, dict):
        return string
    output = json.dumps(string)
    output = output.replace('"', '')
    return output


def sort_diff(diff):
    for key in diff:
        diff[key] = dict(sorted(diff[key].items()))
    return dict(sorted(diff.items()))


def build_diff(old_data, new_data, diff={}):
    merged_keys = old_data.keys() | new_data.keys()
    for key in merged_keys:
        if key not in new_data:
            diff[key] = {'value': format_data(old_data[key]),
                         'status': 'removed'}
        elif key not in old_data:
            diff[key] = {'value': format_data(new_data[key]),
                         'status': 'added'}
        elif new_data[key] == old_data[key]:
            diff[key] = {'value': format_data(new_data[key]),
                         'status': 'unchanged'}
        elif type(old_data[key]) == dict and type(new_data[key]) == dict:
            diff[key] = {}
            build_diff(old_data[key], new_data[key], diff[key])
        else:
            diff[key] = {'value': {'old': format_data(old_data[key]),
                                   'new': format_data(new_data[key])},
                         'status': 'changed'}
    return sort_diff(diff)


def generate_diff(file_path1, file_path2, formatter=stylish):
    file1, file2 = get_data(file_path1, file_path2)
    diff = build_diff(file1, file2, {})
    return formatter(diff)


if __name__ == '__main__':
    generate_diff()
