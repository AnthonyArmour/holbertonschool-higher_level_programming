#!/usr/bin/python3
"""
add_integer returns sum
"""


def add_integer(a, b=98):
    """
    returns a + b
    """
    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)
    if type(a) is not int:
        raise TypeError("a must be an integer")
    elif type(b) is not int:
        raise TypeError("b must be an integer")
    else:
        return int((a + b))
