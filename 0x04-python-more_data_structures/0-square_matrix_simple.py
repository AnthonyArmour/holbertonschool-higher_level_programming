#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    sq = []
    sq_lst = list()
    for lst in matrix:
        for i in lst:
            sq_lst.append(i**2)
        sq.append(sq_lst.copy())
        sq_lst.clear()
    return sq
