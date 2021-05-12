#!/usr/bin/python3
"""returns json object"""


def from_json_string(my_str):
    """returns json object"""
    import json
    return json.loads(my_str)
