from .stylish import stylish
from .plain import plain
from .json import format_as_json


def format_diff(diff, formatter):
    if formatter == 'plain':
        return plain(diff)
    elif formatter == 'json':
        return format_as_json(diff)
    elif formatter == 'stylish' or formatter is None:
        return stylish(diff)
    else:
        raise Exception("Inexistent output formatter, please use 'plain', "
                        "'stylish' or none which equals to 'stylish'")
