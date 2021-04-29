#!/usr/bin/python3
def best_score(a_dictionary):
    sig = None
    num = None
    name = None
    if a_dictionary:
        for k, v in a_dictionary.items():
            if num == None or v > num:
                num = v
                name = k
        return name
    else:
        return None
