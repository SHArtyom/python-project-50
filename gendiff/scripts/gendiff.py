#!/usr/bin/python3
import os
from gendiff.generate_diff import generate_diff
from gendiff.parser import parse_args


def main():
    args = parse_args()
    file1_path = os.path.abspath(args.file_path1)
    file2_path = os.path.abspath(args.file_path2)
    print(generate_diff(file1_path, file2_path))
    return


if __name__ == '__main__':
    main()
