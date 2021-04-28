#!/usr/bin/python3
from sys import argv
tot = 0
if __name__ == "__main__":
    for n in argv[1:]:
        tot = tot + int(n)
    print("{}".format(tot))
