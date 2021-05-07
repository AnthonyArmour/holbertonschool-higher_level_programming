#!/usr/bin/python3
"""replaces ?.: with a \n"""


def text_indentation(text):
    """relaces .?: with \n"""
    sen = ":?."
    x = 0
    if type(text) is not str:
        raise TypeError("text must be a string")
    else:
        while x < int(len(text)):
            print("{}".format(text[x]), end="")
            if text[x] in sen:
                print("{}".format("\n"))
                if text[x + 1] == " " or text[x + 1] == "\t":
                    while text[x + 1] == " ":
                        x += 1
            x += 1
