#!/usr/bin/python3
def uppercase(str1):
    for n in str1:
        if n >= 'a' and n <= 'z':
            n = chr(ord(n) - 32)
        print("{}".format(n), end="")
    print()
