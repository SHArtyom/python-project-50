from gendiff.generate_diff import generate_diff
import os
import json


def test_generate_diff():
    file1 = os.path.abspath('tests/fixtures/file1.json')
    file2 = os.path.abspath('tests/fixtures/file2.json')
    result_file = os.path.abspath('tests/fixtures/result.json')
    with open(result_file, 'r') as result:
        expected = json.load(result)
    assert generate_diff(file1, file2) == expected
