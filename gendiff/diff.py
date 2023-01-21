from gendiff.file_parser import parse_file
from gendiff.build_diff import build_diff
from gendiff.formatters.format_diff import format_diff


def generate_diff(file_path1, file_path2, formatter='stylish'):
    file1 = parse_file(file_path1)
    file2 = parse_file(file_path2)
    diff = build_diff(file1, file2, {})
    return format_diff(formatter, diff)
