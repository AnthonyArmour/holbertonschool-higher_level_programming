#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
from sys import argv
if __name__ == "__main__":
    f1 = 'Unknown operator. Available operators: +, -, * and /'
    if len(argv) != 4:
        print("{}".format('Usage: ./100-my_calculator.py <a> <operator> <b>'))
        exit(1)
    elif (argv[2] != "*" and argv[2] != "+" and
          argv[2] != "/" and argv[2] != "-"):
        print("{}".format(f1))
        exit(1)
    else:
        a = int(argv[1])
        b = int(argv[3])
        if argv[2] == '+':
            print("{} + {} = {}".format(argv[1], argv[3], add(a, b)))
        elif argv[2] == '-':
            print("{} - {} = {}".format(argv[1], argv[3], sub(a, b)))
        elif argv[2] == '*':
            print("{} * {} = {}".format(argv[1], argv[3], mul(a, b)))
        elif argv[2] == '/':
            print("{} / {} = {}".format(argv[1], argv[3], div(a, b)))
