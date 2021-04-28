#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    newlist = list()
    if idx < 0 or idx > len(my_list):
        return my_list
    else:
        for n in range(len(my_list)):
            if n == idx:
                newlist.append(element)
            else:
                newlist.append(my_list[n])
        return newlist
