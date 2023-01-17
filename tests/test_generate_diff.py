import pytest
from gendiff.build_diff import generate_diff

json_flat_old = 'tests/fixtures/file1.json'
json_flat_new = 'tests/fixtures/file2.json'
yml_flat_old = 'tests/fixtures/file1.yml'
yml_flat_new = 'tests/fixtures/file2.yml'
json_tree_old = 'tests/fixtures/tree_file1.json'
json_tree_new = 'tests/fixtures/tree_file2.json'
yaml_tree_old = 'tests/fixtures/tree_file1.yaml'
yaml_tree_new = 'tests/fixtures/tree_file2.yaml'
stylish_flat_result = 'tests/fixtures/stylish_flat_result.txt'
plain_flat_result = 'tests/fixtures/plain_flat_result.txt'
json_flat_result = 'tests/fixtures/json_flat_result.txt'
stylish_tree_result = 'tests/fixtures/stylish_tree_result.txt'
plain_tree_result = 'tests/fixtures/plain_tree_result.txt'
json_tree_result = 'tests/fixtures/json_tree_result.txt'


@pytest.fixture
def get_result():
    def _get_result(format):
        with open(format, 'r') as result:
            expected = result.read()
        return expected
    return _get_result


def test_generate_diff_stylish(get_result):
    assert generate_diff(json_flat_old, json_flat_new, 'stylish') == get_result(stylish_flat_result)[:-1]
    assert generate_diff(yml_flat_old, yml_flat_new, 'stylish') == get_result(stylish_flat_result)[:-1]
    assert generate_diff(json_tree_old, json_tree_new, 'stylish') == get_result(stylish_tree_result)[:-1]
    assert generate_diff(yaml_tree_old, yaml_tree_new, 'stylish') == get_result(stylish_tree_result)[:-1]


def test_generate_diff_plain(get_result):
    assert generate_diff(json_flat_old, json_flat_new, 'plain') == get_result(plain_flat_result)[:-1]
    assert generate_diff(yml_flat_old, yml_flat_new, 'plain') == get_result(plain_flat_result)[:-1]
    assert generate_diff(json_tree_old, json_tree_new, 'plain') == get_result(plain_tree_result)[:-1]
    assert generate_diff(yaml_tree_old, yaml_tree_new, 'plain') == get_result(plain_tree_result)[:-1]


def test_generate_diff_json(get_result):
    assert generate_diff(json_flat_old, json_flat_new, 'json') == get_result(json_flat_result)[:-1]
    assert generate_diff(yml_flat_old, yml_flat_new, 'json') == get_result(json_flat_result)[:-1]
    assert generate_diff(json_tree_old, json_tree_new, 'json') == get_result(json_tree_result)[:-1]
    assert generate_diff(yaml_tree_old, yaml_tree_new, 'json') == get_result(json_tree_result)[:-1]
