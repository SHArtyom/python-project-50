from gendiff.generate_diff import generate_diff
import os


file1 = os.path.abspath('tests/fixtures/file1.json')
file2 = os.path.abspath('tests/fixtures/file2.json')
file3 = os.path.abspath('tests/fixtures/file1.yml')
file4 = os.path.abspath('tests/fixtures/file2.yml')
expected = """
{
  - follow: false
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: true
}
"""


def test_generate_diff():
    assert generate_diff(file1, file2) == expected[1:-1]
    assert generate_diff(file3, file4) == expected[1:-1]
