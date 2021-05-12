#!/usr/bin/python3
"""reads stdin and computes metrics"""


import sys

x = 0
size = 0
d = {
    '200': 0,
    '301': 0,
    '400': 0,
    '401': 0,
    '403': 0,
    '404': 0,
    '405': 0,
    '500': 0
}
try:
    for line in sys.stdin:
        x += 1
        lst = line.split()
        if len(lst) < 3:
            lst.clear()
            continue
        if lst[-2] in d.keys():
            d[lst[-2]] += 1
            size += int(lst[-1])
        if x == 10:
            x = 0
            print("File size: {}".format(size))
            for status in sorted(d.keys()):
                if d[status] > 0:
                    print("{}: {}".format(status, d[status]))
        lst.clear
    if x < 10:
        print("File size: {}".format(size))
        for status in sorted(d.keys()):
            if d[status] > 0:
                print("{}: {}".format(status, d[status]))
except KeyboardInterrupt:
    print("File size: {}".format(size))
    for status in sorted(d.keys()):
        if d[status] > 0:
            print("{}: {}".format(status, d[status]))
