from gendiff.generate_diff import generate_diff
import os
import json
import pytest

def test_generate_diff():
    file1 = os.path.abspath(files/file1.json)
    file2 = os.path.abspath(files/file2.json)
    result_file = os.path.abspath(files/result.json)
    with open(result_file) as result:
        expected = json.loads(result)
    assert generate_diff(file1, file2) == expected
