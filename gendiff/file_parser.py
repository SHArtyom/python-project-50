import json
import yaml
import pathlib
from yaml import SafeLoader


def read_file(file_path):
    extension = pathlib.Path(file_path).suffix
    file = open(file_path, 'r')
    return file, extension


def get_file_content(input_data):
    file, extension = input_data
    if extension == '.json':
        output = json.load(file)
    elif extension == '.yaml' or extension == '.yml':
        output = yaml.load(file, Loader=SafeLoader)
    return output


def parse_file(file_path):
    return get_file_content(read_file(file_path))
