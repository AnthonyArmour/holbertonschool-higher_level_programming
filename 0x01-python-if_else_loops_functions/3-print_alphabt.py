#!/usr/bin/python3
for n in 'abcdfghijklmnoprstuvwxyz':
    if n == 'q' or n == 'e':
        continue
    print("{}".format(n), end="")
