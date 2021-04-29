#!/usr/bin/python3
def search_replace(my_list, search, replace):
    n = 0
    nlst = list()
    while n < len(my_list):
        if my_list[n] == search:
            nlst.append(int(replace))
        else:
            nlst.append(my_list[n])
        n = n + 1
    return nlst
