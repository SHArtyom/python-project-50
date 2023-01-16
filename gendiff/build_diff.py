import json
import yaml
from yaml import SafeLoader
from gendiff.formatters.stylish import stylish
from gendiff.formatters.plain import plain
from gendiff.formatters.json import format_as_json


def parse_file(file_path):
    if '.json' in file_path[-6:]:
        with open(file_path, 'r') as f:
            file = json.load(f)
    elif '.yaml' or '.yml' in file_path[-6:]:
        with open(file_path, 'r') as f:
            file = yaml.load(f, Loader=SafeLoader)
    return file


def format_data(string):
    if isinstance(string, dict):
        return string
    output = json.dumps(string)
    output = output.replace('"', '')
    return output


def build_diff(old_data, new_data, diff={}):
    merged_keys = old_data.keys() | new_data.keys()
    for key in sorted(merged_keys):
        if key not in new_data:
            diff[key] = {'value': old_data[key],
                         'status': 'removed'}
        elif key not in old_data:
            diff[key] = {'value': new_data[key],
                         'status': 'added'}
        elif new_data[key] == old_data[key]:
            diff[key] = {'value': new_data[key],
                         'status': 'unchanged'}
        elif type(old_data[key]) == dict and type(new_data[key]) == dict:
            diff[key] = {}
            build_diff(old_data[key], new_data[key], diff[key])
        else:
            diff[key] = {'value': {'old': old_data[key],
                                   'new': new_data[key]},
                         'status': 'changed'}
    return diff


def generate_diff(file_path1, file_path2, formatter='stylish'):
    file1 = parse_file(file_path1)
    file2 = parse_file(file_path2)
    diff = build_diff(file1, file2, {})
    if formatter == 'plain':
        return plain(diff)
    elif formatter == 'json':
        return format_as_json(diff)
    else:
        return stylish(diff)
