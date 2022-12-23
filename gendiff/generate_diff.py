import json
from copy import deepcopy


def generate_diff(file_path1, file_path2):
    file1 = json.load(open(file_path1))
    file2 = json.load(open(file_path2))
    output_string = ''
    new_line = '\n'
    new_dict = deepcopy(file1)
    new_dict.update(file2)
    new_dict = dict(sorted(new_dict.items()))
    for key in new_dict:
        if file1.get(key) == file2.get(key):
            output_string += f'    {key}: {new_dict[key]}{new_line}'
        elif key not in file1:
            output_string += f'  + {key}: {new_dict[key]}{new_line}'
        elif key not in file2:
            output_string += f'  - {key}: {new_dict[key]}{new_line}'
        else:
            output_string += f'  - {key}: {file1[key]}{new_line}'
            output_string += f'  + {key}: {new_dict[key]}{new_line}'
    output_string = '{\n' + output_string + '}'
    return output_string


if __name__ == '__main__':
    generate_diff()
