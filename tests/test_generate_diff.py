from gendiff.build_diff import generate_diff
from gendiff.formatters.plain import plain
from gendiff.formatters.stylish import stylish
from gendiff.formatters.json import format_as_json
import os
import json


file1 = os.path.abspath('tests/fixtures/file1.json') #json flat old_data
file2 = os.path.abspath('tests/fixtures/file2.json') #json flat new_data
file3 = os.path.abspath('tests/fixtures/file1.yml') #yml flat old_data
file4 = os.path.abspath('tests/fixtures/file2.yml') #yml flat new_data
file5 = os.path.abspath('tests/fixtures/tree_file1.json') #json tree old_data
file6 = os.path.abspath('tests/fixtures/tree_file2.json') #json tree new_data
file7 = os.path.abspath('tests/fixtures/tree_file1.yaml') #yaml tree old_data
file8 = os.path.abspath('tests/fixtures/tree_file2.yaml') #yaml tree new_data
flat_result = os.path.abspath('tests/fixtures/flat_result.txt') #txt flat result
stylish_result = os.path.abspath('tests/fixtures/stylish_result.txt') #txt tree stylish result
plain_result = os.path.abspath('tests/fixtures/plain_result.txt') #txt tree plain format result
json_result = os.path.abspath('tests/fixtures/json_result.txt') #txt tree json format result

with open(flat_result, 'r') as result:
    expected_flat = result.read()

with open(stylish_result, 'r') as result:
    expected_stylish = result.read()

with open(plain_result, 'r') as result:
    expected_plain = result.read()

with open(json_result, 'r') as result:
    expected_json = result.read()

def test_generate_diff():
    assert generate_diff(file1, file2, stylish) == expected_flat[:-1]
    assert generate_diff(file3, file4, stylish) == expected_flat[:-1]
    assert generate_diff(file5, file6, stylish) == expected_stylish[:-1]
    assert generate_diff(file7, file8, stylish) == expected_stylish[:-1]
    assert generate_diff(file5, file6, plain) == expected_plain
    assert generate_diff(file7, file8, plain) == expected_plain
    assert generate_diff(file5, file6, format_as_json) == expected_json[:-1]
    assert generate_diff(file7, file8, format_as_json) == expected_json[:-1]
