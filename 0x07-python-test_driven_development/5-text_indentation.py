#!/usr/bin/python3
def text_indentation(text):
    sen = ":?."
    if type(text) is not str:
        raise TypeError("text must be a string")
    else:
        for x in range(int(len(text))):
            if text[x - 1] in sen:
                print("{}".format("\n"))
            else:
                print("{}".format(text[x]), end="")
