### Hexlet tests and linter status:
[![Actions Status](https://github.com/SHArtyom/python-project-50/workflows/hexlet-check/badge.svg)](https://github.com/SHArtyom/python-project-50/actions)
[![Python CI](https://github.com/SHArtyom/python-project-50/actions/workflows/Python-CI.yml/badge.svg)](https://github.com/SHArtyom/python-project-50/actions/workflows/Python-CI.yml)
[![Maintainability](https://api.codeclimate.com/v1/badges/39f82bf32739fa9427e6/maintainability)](https://codeclimate.com/github/SHArtyom/python-project-50/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/39f82bf32739fa9427e6/test_coverage)](https://codeclimate.com/github/SHArtyom/python-project-50/test_coverage)
____

# Description

This package is a tool to search and list differences between JSON and YAML files

## Program demo
Help message and flat structure processing
[![asciicast](https://asciinema.org/a/ZeE9qGo90bBKHLxejH9He9jUz.svg)](https://asciinema.org/a/ZeE9qGo90bBKHLxejH9He9jUz)

Nested structure processing with stylish output
[![asciicast](https://asciinema.org/a/0bXK8SsGKAjG2PfFhBTUGXrIK.svg)](https://asciinema.org/a/0bXK8SsGKAjG2PfFhBTUGXrIK)

Nested structure processing with plain output
[![asciicast](https://asciinema.org/a/qcMSZTi9eAi2qv1Tr7Bea7P2O.svg)](https://asciinema.org/a/qcMSZTi9eAi2qv1Tr7Bea7P2O)

Nested structure processing with json output
[![asciicast](https://asciinema.org/a/ARs22hAxq8ng7SocuxbDe1d0f.svg)](https://asciinema.org/a/ARs22hAxq8ng7SocuxbDe1d0f)

## Minimum requirements

`python3.8`

## Installation

### To install the package for an end-user

Execute:

`python3 -m pip install --user dist/*.whl`

### If you would like to install it as a developer

To install all dependencies execute:

`make install`

To build a package execute:

`make build`

To install the package execute:

`make package-install`
