from gendiff.generate_diff import generate_diff
import os
import json


file1 = os.path.abspath('tests/fixtures/file1.json')
file2 = os.path.abspath('tests/fixtures/file2.json')
file3 = os.path.abspath('tests/fixtures/file1.yml')
file4 = os.path.abspath('tests/fixtures/file2.yml')
file5 = os.path.abspath('tests/fixtures/tree_file1.json')
file6 = os.path.abspath('tests/fixtures/tree_file2.json')
file7 = os.path.abspath('tests/fixtures/tree_file1.yaml')
file8 = os.path.abspath('tests/fixtures/tree_file2.yaml')

expected_plain = """
{
  - follow: false
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: true
}
"""

expected_tree = """
{
    common: {
      + follow: false
        setting1: Value 1
      - setting2: 200
      - setting3: true
      + setting3: null
      + setting4: blah blah
      + setting5: {
            key5: value5
        }
        setting6: {
            doge: {
              - wow:
              + wow: so much
            }
            key: value
          + ops: vops
        }
    }
    group1: {
      - baz: bas
      + baz: bars
        foo: bar
      - nest: {
            key: value
        }
      + nest: str
    }
  - group2: {
        abc: 12345
        deep: {
            id: 45
        }
    }
  + group3: {
        deep: {
            id: {
                number: 45
            }
        }
        fee: 100500
    }
}"""


def test_generate_diff_plain():
    assert generate_diff(file1, file2) == expected_plain[1:-1]
    assert generate_diff(file3, file4) == expected_plain[1:-1]
    assert generate_diff(file5, file6) == expected_tree
    assert generate_diff(file7, file8) == expected_tree

