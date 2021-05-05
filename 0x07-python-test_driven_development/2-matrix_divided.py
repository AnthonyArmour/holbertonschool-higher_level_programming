#!/usr/bin/python3
def matrix_divided(matrix, div):
    """divides every element of matrix by div"""
    sq = []
    sq_lst = list()
    em = "matrix must be a matrix (list of lists) of integers/floats"
    ed = "div must be a number"
    es = "Each row of the matrix must have the same size"
    if type(div) is not int and type(div) is not float:
        raise TypeError(ed)
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if type(matrix) is not list or type(matrix[0]) is not list:
        raise TypeError(em)
    size = len(matrix[0])
    for lst in matrix:
        if type(lst) is not list:
            raise TypeError(em)
        if len(lst) != size:
            raise TypeError(es)
        for i in lst:
            sq_lst.append(round(i / div, 2))
        sq.append(sq_lst.copy())
        sq_lst.clear()
    return sq
