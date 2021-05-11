#!/usr/bin/python3
"""returns true if same class"""


def is_same_class(obj, a_class):
    if a_class.__name__ == "object":
        return False
    if isinstance(obj, a_class):
        return True
    else:
        return False
