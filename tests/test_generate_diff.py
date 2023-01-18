import pytest
from gendiff.diff_output import generate_diff

JSON_FLAT_OLD = 'tests/fixtures/file1.json'
JSON_FLAT_NEW = 'tests/fixtures/file2.json'
YML_FLAT_OLD = 'tests/fixtures/file1.yml'
YML_FLAT_NEW = 'tests/fixtures/file2.yml'
JSON_TREE_OLD = 'tests/fixtures/tree_file1.json'
JSON_TREE_NEW = 'tests/fixtures/tree_file2.json'
YAML_TREE_OLD = 'tests/fixtures/tree_file1.yaml'
YAML_TREE_NEW = 'tests/fixtures/tree_file2.yaml'
STYLISH_FLAT_RESULT = 'tests/fixtures/stylish_flat_result.txt'
PLAIN_FLAT_RESULT = 'tests/fixtures/plain_flat_result.txt'
JSON_FLAT_RESULT = 'tests/fixtures/json_flat_result.txt'
STYLISH_TREE_RESULT = 'tests/fixtures/stylish_tree_result.txt'
PLAIN_TREE_RESULT = 'tests/fixtures/plain_tree_result.txt'
JSON_TREE_RESULT = 'tests/fixtures/json_tree_result.txt'


@pytest.fixture
def get_result():
    def _get_result(format):
        with open(format, 'r') as result:
            expected = result.read()
        return expected.rstrip('\n')
    return _get_result


def test_generate_diff_stylish(get_result):
    assert generate_diff(JSON_FLAT_OLD, JSON_FLAT_NEW, 'stylish') == get_result(STYLISH_FLAT_RESULT)
    assert generate_diff(YML_FLAT_OLD, YML_FLAT_NEW, 'stylish') == get_result(STYLISH_FLAT_RESULT)
    assert generate_diff(JSON_TREE_OLD, JSON_TREE_NEW, 'stylish') == get_result(STYLISH_TREE_RESULT)
    assert generate_diff(YAML_TREE_OLD, YAML_TREE_NEW, 'stylish') == get_result(STYLISH_TREE_RESULT)


def test_generate_diff_plain(get_result):
    assert generate_diff(JSON_FLAT_OLD, JSON_FLAT_NEW, 'plain') == get_result(PLAIN_FLAT_RESULT)
    assert generate_diff(YML_FLAT_OLD, YML_FLAT_NEW, 'plain') == get_result(PLAIN_FLAT_RESULT)
    assert generate_diff(JSON_TREE_OLD, JSON_TREE_NEW, 'plain') == get_result(PLAIN_TREE_RESULT)
    assert generate_diff(YAML_TREE_OLD, YAML_TREE_NEW, 'plain') == get_result(PLAIN_TREE_RESULT)


def test_generate_diff_json(get_result):
    assert generate_diff(JSON_FLAT_OLD, JSON_FLAT_NEW, 'json') == get_result(JSON_FLAT_RESULT)
    assert generate_diff(YML_FLAT_OLD, YML_FLAT_NEW, 'json') == get_result(JSON_FLAT_RESULT)
    assert generate_diff(JSON_TREE_OLD, JSON_TREE_NEW, 'json') == get_result(JSON_TREE_RESULT)
    assert generate_diff(YAML_TREE_OLD, YAML_TREE_NEW, 'json') == get_result(JSON_TREE_RESULT)
