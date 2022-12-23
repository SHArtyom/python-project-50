#!/usr/bin/python3
import argparse
import os
from gendiff.generate_diff import generate_diff


def main():
    parser = argparse.ArgumentParser(description='Compares two configuration'
                                     'files and shows a difference.')
    parser.add_argument('file_path1', type=str)
    parser.add_argument('file_path2', type=str)
    parser.add_argument('-f', '--format', type=str, help='set format of output')
    args = parser.parse_args()
    file1_path = os.path.abspath(args.file_path1)
    file2_path = os.path.abspath(args.file_path2)
    print(generate_diff(file1_path, file2_path))
    return


if __name__ == '__main__':
    main()
