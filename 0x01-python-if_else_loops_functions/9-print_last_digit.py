#!/usr/bin/python3
def print_last_digit(num):
    if num < 0:
        num = num * -1
    while num > 9:
        num = num % 10
    print("{}".format(num), end="")
    return num
