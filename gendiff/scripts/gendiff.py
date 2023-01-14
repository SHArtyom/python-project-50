#!/usr/bin/python3
import os
from gendiff.build_diff import generate_diff
from gendiff.parser import parse_args
from gendiff.formatters.plain import plain
from gendiff.formatters.stylish import stylish
from gendiff.formatters.json import format_as_json


def main():
    args = parse_args()
    file1_path = os.path.abspath(args.file_path1)
    file2_path = os.path.abspath(args.file_path2)
    if args.format == 'plain':
        formatter = plain
    elif args.format == 'json':
        formatter = format_as_json
    else:
        formatter = stylish
    result = generate_diff(file1_path, file2_path, formatter)
    print(result)
    return


if __name__ == '__main__':
    main()
