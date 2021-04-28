#!/usr/bin/python3
from sys import argv
x = 1
if __name__ == "__main__":
    if len(argv) < 2:
        print("{}".format('0 arguments.'))
    else:
        if len(argv) == 2:
            print("{}".format('1 argument:'))
        else:
            print("{} arguments:".format(len(argv) - 1))
        for n in argv[1:]:
            print("{}: {}".format(x, n))
            x = x + 1
