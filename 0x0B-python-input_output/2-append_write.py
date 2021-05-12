#!/usr/bin/python3
"""append text to a file"""


def append_write(filename="", text=""):
    """appends text to a file"""
    with open(filename, "a+") as fh:
        try:
            fh.write(text)
        except:
            count = 0
        else:
            count = len(text)
    return count
