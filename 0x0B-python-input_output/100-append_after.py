#!/usr/bin/python3
"""inserts new_string under search string"""


def append_after(filename="", search_string="", new_string=""):
    """appends after search string"""
    st = ""
    with open(filename, "r") as fh:
        for line in fh:
            st = st + str(line)
            if search_string in line:
                st = st + new_string
    with open(filename, "w+") as fh:
        fh.write(st)
