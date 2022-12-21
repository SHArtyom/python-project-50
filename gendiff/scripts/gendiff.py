#!/usr/bin/python3
import argparse
import json
from copy import deepcopy
import os


def main():
    parser = argparse.ArgumentParser(description='Compares two configuration files and shows a difference.')
    parser.add_argument('file_path1', type=str)
    parser.add_argument('file_path2', type=str)
    parser.add_argument('-f', '--format', type=str, help='set format of output')
    args = parser.parse_args()
    file1_path = os.path.abspath(args.file_path1)
    file2_path = os.path.abspath(args.file_path2)
    print(generate_diff(file1_path, file2_path))
    return


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
            output_string += f'  {key}: {new_dict[key]}{new_line}'
        elif key not in file1:
            output_string += f'+ {key}: {new_dict[key]}{new_line}'
        elif key not in file2:
            output_string += f'- {key}: {new_dict[key]}{new_line}'
        else:
            output_string += f'- {key}: {file1[key]}{new_line}+ {key}: {new_dict[key]}{new_line}'
    output_string = '{\n' + output_string + '}'
    return output_string


if __name__ == '__main__':
    main()
