#!/usr/bin/python3
"""say my name module"""


def say_my_name(first_name, last_name=""):
    """this module says name"""
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    if last_name is None and first_name is None:
        print()
    elif last_name is not None:
        print("My name is {} {}".format(first_name, last_name))
    else:
        print("My name is {}".format(first_name))
