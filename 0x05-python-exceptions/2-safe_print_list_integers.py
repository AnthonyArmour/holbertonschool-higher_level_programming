#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    tot = 0
    i = 0
    while i < x:
        try:
            print("{:d}".format(my_list[i]), end="")
            tot = tot + 1
            i = i + 1
        except (ValueError, TypeError) as error:
            i = i + 1
            continue
    print()
    return tot
