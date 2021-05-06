#!/usr/bin/python3
"""prints square of #"""


def print_square(size):
    """prints a square of #"""
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if type(size) is float and size < 0:
        raise TypeError("size must be an integer")
    else:
        for i in range(size):
            print("{}".format("#") * size)
