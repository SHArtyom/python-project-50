from gendiff.generate_diff import generate_diff
import os
import json


file1 = os.path.abspath('tests/fixtures/file1.json') #json plain old_data
file2 = os.path.abspath('tests/fixtures/file2.json') #json plain new_data
file3 = os.path.abspath('tests/fixtures/file1.yml') #yml plain old_data
file4 = os.path.abspath('tests/fixtures/file2.yml') #yml plain new_data
file5 = os.path.abspath('tests/fixtures/tree_file1.json') #json tree old_data
file6 = os.path.abspath('tests/fixtures/tree_file2.json') #json tree new_data
file7 = os.path.abspath('tests/fixtures/tree_file1.yaml') #yaml tree old_data
file8 = os.path.abspath('tests/fixtures/tree_file2.yaml') #yaml tree new_data
plain_result = os.path.abspath('tests/fixtures/plain_result.txt') #txt plain result
tree_result = os.path.abspath('tests/fixtures/tree_result.txt') #txt tree result


with open(plain_result, 'r') as result:
    expected_plain = result.read()

with open(tree_result, 'r') as result:
    expected_tree = result.read()



def test_generate_diff():
    assert generate_diff(file1, file2) == expected_plain[:-1]
    assert generate_diff(file3, file4) == expected_plain[:-1]
    assert generate_diff(file5, file6) == expected_tree[:-1]
    assert generate_diff(file7, file8) == expected_tree[:-1]
