#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    if a_dictionary is None:
        return None
    lst = list()
    for k, v in a_dictionary.items():
            if v == value:
                lst.append(k)
    for i in lst:
        del a_dictionary[i]
    return a_dictionary
