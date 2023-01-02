import json
import yaml
from yaml import SafeLoader
from copy import deepcopy


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


def generate_diff(file_path1, file_path2):
    file1, file2 = get_data(file_path1, file_path2)
    new_dict = deepcopy(file1)
    new_dict.update(file2)
    new_dict = dict(sorted(new_dict.items()))
    diff_dict = {}
    for key in new_dict:
        if file1.get(key) == file2.get(key):
            diff_dict[f'  {key}'] = new_dict[key]
        elif key not in file1:
            diff_dict[f'+ {key}'] = new_dict[key]
        elif key not in file2:
            diff_dict[f'- {key}'] = new_dict[key]
        else:
            diff_dict[f'- {key}'] = file1[key]
            diff_dict[f'+ {key}'] = new_dict[key]
    result = json.dumps(diff_dict, indent=2)
    result = result.replace(',', '').replace('"', '')
    return result


if __name__ == '__main__':
    generate_diff()
