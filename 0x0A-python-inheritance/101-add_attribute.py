#!/usr/bin/python3
"""adds attribute to object"""


def add_attribute(obj, name, value):
    if getattr(obj, "__dict__", 5) != 5:
        setattr(obj, name, value)
    else:
        raise TypeError("can't add new attribute'")
