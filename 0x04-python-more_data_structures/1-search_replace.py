#!/usr/bin/python3
def search_replace(my_list, search, replace):
    n = 0
    nlst = list()
    while n < len(my_list):
        nlst.append(my_list[n])
        if my_list[n] == search:
            nlst.append(replace)
        n = n + 1
    return nlst
