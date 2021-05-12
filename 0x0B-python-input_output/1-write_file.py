#!/usr/bin/python3
"""writes do file"""


def write_file(filename="", text=""):
    """writes to file"""
    with open(filename, "w+") as fh:
        try:
            fh.write(text)
        except:
            count = 0
        else:
            count = len(text)
    return count
