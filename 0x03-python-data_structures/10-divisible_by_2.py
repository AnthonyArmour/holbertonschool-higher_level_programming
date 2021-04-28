#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if not my_list:
        return None
    lst = list()
    for n in my_list:
        if (int(n) % 2) == 0:
            lst.append(True)
        else:
            lst.append(False)
    return lst
