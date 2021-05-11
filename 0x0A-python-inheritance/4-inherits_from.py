#!/usr/bin/python3
"""returns true if same class"""


def inherits_from(obj, a_class):
    """returns True if obj inherited from a_class"""
    if type(obj) == a_class:
        return False
    elif issubclass(type(obj), a_class):
        return True
    else:
        return False
