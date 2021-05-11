#!/usr/bin/python3
"""returns true if same class"""


def is_kind_of_class(obj, a_class):
    """returns true if same class or from inherited from"""
    if issubclass(type(obj), a_class):
        return True
    if type(obj) == a_class:
        return True
    else:
        return False
