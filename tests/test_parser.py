import sys
from gendiff.arg_parser import parse_args


def test_parse_args():
    sys.argv = ['gendiff', '--format', 'plain', 'file1.json', 'file2.json']
    args = parse_args()
    assert args.file_path1 == 'file1.json'
    assert args.file_path2 == 'file2.json'
    assert args.format == 'plain'
