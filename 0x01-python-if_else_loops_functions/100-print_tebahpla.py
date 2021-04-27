#!/usr/bin/python3
for n in reversed("abcdefghijklmnopqrstuvwxyz"):
    if ord(n) % 2 == 0:
        if n < 'a':
            n = chr(ord(n) + 32)
            print("{}".format(n), end="")
        else:
            print("{}".format(n), end="")
    else:
        if n > 'Z':
            n = chr(ord(n) - 32)
            print("{}".format(n), end="")
        else:
            print("{}".format(n), end="")
