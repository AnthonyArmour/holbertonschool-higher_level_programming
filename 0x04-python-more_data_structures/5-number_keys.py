#!/usr/bin/python3
def number_keys(a_dictionary):
    tot = 0
    for k, v in a_dictionary.items():
        if k:
            tot = tot + 1
    return int(tot)
