#!/usr/bin/python3
def max_integer(my_list=[]):
    num = 0
    if not my_list:
        return None
    else:
        for x in my_list:
            if x > num:
                num = x
    return num
