#!/usr/bin/python3
"""This program solves the N queens problem"""


import sys


def solve_n_queens(queens):
    """solves the N Queens problem"""
    if type(queens) is not int:
        raise TypeError("must be an int")
    board = list()
    lst = list()
    y = 0
    for i in range(queens):
        for n in range(queens):
            lst.append(0)
        board.append(list(lst))
        lst.clear()
    inception(board, y)


def inception(board, y, res=False):
    """checks for an (all safe) combo"""
    xx = 0
    if y == len(board):
        print_res(board)
        return
    while xx < len(board):
        if check_safe_spot(board, xx, y):
            board[xx][y] = 1
            res = inception(board, y + 1, res)
            if res is True:
                return True, board
            board[xx][y] = 0
        else:
            res = False
        xx += 1
    return res, board


def check_safe_spot(board, xx, y):
    """checks if current index is safe from other queens"""
    res = True
    yn = 0
    xn = xx

    while xn < len(board):
        while yn < y:
            if board[xn][yn] == 1:
                return False
            yn += 1
        xn += 1
    """checks diagnals"""
    xn = xx - 1
    yn = y - 1
    while yn >= 0 and xn >= 0:
        if board[xn][yn] == 1:
            res = False
        yn -= 1
        xn -= 1
    xn = xx + 1
    yn = y - 1
    while xn < len(board) and yn >= 0:
        if board[xn][yn] == 1:
            res = False
        xn += 1
        yn -= 1
    return res


def print_res(board):
    """prints the index of all safe queens"""
    x = 0
    y = 0
    lst = list()
    matrix = list()
    while x < len(board):
        while y < len(board):
            if board[x][y] == 1:
                lst.append(x)
                lst.append(y)
                matrix.append(list(lst))
                lst.clear()
            y += 1
        y = 0
        x += 1
    print("{}".format(matrix))


if len(sys.argv) != 2:
    print("{}".format("Usage: nqueens N"))
    exit(1)
arg = sys.argv[1]
if not arg.isdigit():
    print("{}".format("N must be a number"))
    exit(1)
if int(arg) < 4:
    print("{}".format("N must be at least 4"))
    exit(1)
solve_n_queens(int(arg))
