#!/usr/bin/python3
"""returns list of integers representing pascals triangle"""


def pascal_triangle(n):
    """pascals triangle method"""
    if n <= 0:
        return list()
    matrix = list()
    lst = list()
    x = 1
    idx = 0
    matrix.append([1])
    for nn in range(n - 1):
        lst.append(1)
        if nn == 0:
            lst.append(1)
            matrix.append(lst[:])
            lst.clear()
            continue
        while idx < len(matrix[x]) - 1:
            num = int(matrix[x][idx]) + int(matrix[x][idx + 1])
            lst.append(num)
            idx += 1
        lst.append(1)
        x += 1
        idx = 0
        matrix.append(lst[:])
        lst.clear()
    return matrix
