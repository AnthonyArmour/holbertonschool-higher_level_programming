#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    sig = 0
    for lst in matrix:
        x = 0
        for n in lst:
            sig = 1
            if x + 1 == len(lst):
                print("{}".format(n))
            else:
                print("{}".format(n), end=" ")
            x = x + 1
    if sig == 0:
        print()
