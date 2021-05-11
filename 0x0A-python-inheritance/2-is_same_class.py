#!/usr/bin/python3
"""returns true if same class"""


def is_same_class(obj, a_class):
    """returns true if same clas"""
    if a_class.__name__ == "object":
        return False
    if type(obj) == a_class:
        return True
    else:
        return False
