#!/usr/bin/python3
for x in range(10):
    for y in range(10):
        if x < y:
            print("{}".format(str(x) + str(y)), end="")
            if not (x == 8 and y == 9):
                print("{}".format(', '), end="")
            else:
                print()
