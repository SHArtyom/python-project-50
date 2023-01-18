import argparse


def parse_args():
    parser = argparse.ArgumentParser(description='Compares two configuration'
                                     'files and shows a difference.')
    parser.add_argument('file_path1', type=str)
    parser.add_argument('file_path2', type=str)
    parser.add_argument('-f', '--format', type=str, help='set format of output')
    args = parser.parse_args()
    return args
