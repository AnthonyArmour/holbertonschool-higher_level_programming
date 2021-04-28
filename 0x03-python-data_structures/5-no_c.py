#!/usr/bin/python3
def no_c(my_string):
    x = 0
    s = ""
    while x < len(my_string):
        if my_string[x] == 'c' or my_string[x] == 'C':
            x = x + 1
            continue
        else:
            s = s + my_string[x]
            x = x + 1
    return s
