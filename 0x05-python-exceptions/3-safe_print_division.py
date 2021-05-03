#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        tot = a / b
    except:
        tot = None
    finally:
        print("Inside result: {}".format(tot))
    return tot
