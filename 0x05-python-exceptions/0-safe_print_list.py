#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    i = 0
    tot = 0
    while i < x:
        try:
            print("{:d}".format(my_list[i]), end="")
            i = i + 1
            tot = tot + 1
        except Exception:
            print()
            return tot
    print()
    return tot
