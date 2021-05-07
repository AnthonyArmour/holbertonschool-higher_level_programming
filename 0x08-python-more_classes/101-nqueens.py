#!/usr/bin/python3
"""This program solves the N queens problem"""


def solve_n_queens(queens):
    """solves the N Queens problem"""
    if type(queens) is not int:
        raise TypeError("must be an int")
    board = list()
    lst = list()
    for i in range(queens):
        for n in range(queens):
            lst.append(0)
        board.append(list(lst))
        lst.clear()
    solutionQ(board)



def solutionQ(board):
    mlen = len(board)
    x = 1
    y = 1
    res = False
    while x < len(board) - 1:
        board[x][0] = 1
        res, board = inception(board, y, res)
        if res is not False:
            print_res(board)
        board = reset_board(board)
        x += 1
        res = False

def inception(board, y, res):
    xx = 0
    res = False
    if y == len(board):
        return True, board
    while xx < len(board):
        if check_safe_spot(board, xx, y):
            board[xx][y] = 1
            res, board = inception(board, y + 1, res)
            if res is True:
                return True, board
            board[xx][y] = 0
        else:
            res = False
        xx += 1
    return res, board

def check_safe_spot(board, xx, y):
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
    while xn < len(board) and y >= 0:
        if board[xn][yn] == 1:
            res = False
        xn += 1
        yn -= 1
    return res

def print_res(board):
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

def reset_board(board):
    """resets the board"""
    x = 0
    y = 0
    while x < len(board):
        while y < len(board):
            board[x][y] = 0
            y += 1
        y = 0
        x += 1
    return board

solve_n_queens(4)
