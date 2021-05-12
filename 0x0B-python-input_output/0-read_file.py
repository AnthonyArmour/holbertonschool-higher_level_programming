#!/usr/bin/python3
"""reads file and prints to stdout"""


def read_file(filename=""):
    """reads a file and prints to stdout"""
    with open(filename) as fh:
        for line in fh:
            print("{}".format(line), end="")
