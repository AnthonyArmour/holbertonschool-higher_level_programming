#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list is None:
        return 0
    tot = 0
    div = 0
    for i in my_list:
        tot = tot + (int(i[0]) * int(i[1]))
        div = div + int(i[1])
    return float(tot / div)
