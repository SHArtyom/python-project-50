from gendiff.formatters.stylish import stylish
from gendiff.formatters.plain import plain
from gendiff.formatters.json import format_as_json
from gendiff.file_parser import parse_file
from gendiff.build_diff import build_diff


def generate_diff(file_path1, file_path2, formatter='stylish'):
    file1 = parse_file(file_path1)
    file2 = parse_file(file_path2)
    diff = build_diff(file1, file2, {})
    if formatter == 'plain':
        return plain(diff)
    elif formatter == 'json':
        return format_as_json(diff)
    else:
        return stylish(diff)
