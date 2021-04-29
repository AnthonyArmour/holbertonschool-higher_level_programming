#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    lst = list()
    for i in set_1:
        if i in set_2:
            continue
        else:
            lst.append(i)
    for n in set_2:
        if n in set_1 or n in lst:
            continue
        else:
            lst.append(n)
    return lst
