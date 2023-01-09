#!/usr/bin/python3
import os
from gendiff.generate_diff import generate_diff, stylish
from gendiff.parser import parse_args
import json

def main():
    args = parse_args()
    file1_path = os.path.abspath(args.file_path1)
    file2_path = os.path.abspath(args.file_path2)
    formatter = stylish
    result = generate_diff(file1_path, file2_path, formatter)
    print(result)
    return


if __name__ == '__main__':
    main()
