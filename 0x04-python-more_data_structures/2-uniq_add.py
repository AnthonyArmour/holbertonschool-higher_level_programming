#!/usr/bin/python3
def uniq_add(my_list=[]):
    lst = list()
    tot = 0
    for n in my_list:
        if n not in lst:
            lst.append(n)
    for i in lst:
        tot = tot + i
    return tot
