#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    d = dict()
    for k, v in a_dictionary.items():
        d[k] = int(v * 2)
    return d
