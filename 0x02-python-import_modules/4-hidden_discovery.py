#!/usr/bin/python3
import hidden_4
if __name__ == "__main__":
    for n in dir(hidden_4):
        if n.startswith("__"):
            continue
        else:
            print("{}".format(n))
