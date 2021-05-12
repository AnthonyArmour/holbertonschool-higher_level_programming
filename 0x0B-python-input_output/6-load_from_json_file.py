#!/usr/bin/python3
"""returns object from read json file"""


def load_from_json_file(filename):
    """returns object from json file"""
    import json
    with open(filename) as fh:
        file_str = fh.read()
        return json.loads(file_str)
