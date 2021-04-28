#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list is not None:
        num = my_list[0]
        for x in my_list:
            if x > num:
                num = x
        return num
    return None
