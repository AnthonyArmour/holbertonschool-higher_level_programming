#!/usr/bin/python3
def roman_to_int(roman_string):
    ints = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000]
    lets = ["I", "IV", "V", "IX", "X",
            "XL", "L", "XC", "C", "CD", "D", "CM", "M"]
    idx = 0
    d = dict()
    while idx < 13:
        d[lets[idx]] = ints[idx]
        idx = idx + 1
    x = 0
    tot = 0
    if roman_string is None or type(roman_string) != str:
        return 0
    rstr = ""
    rstr = rstr + roman_string
    if len(rstr) == 1:
        if rstr in d.keys():
            return int(d[rstr])
        else:
            return 0
    while x < len(rstr) - 1:
        st = rstr[x] + rstr[x + 1]
        if st in d.keys():
            tot = tot + d[st]
            x = x + 2
            continue
        elif st[0] in d.keys():
            tot = tot + d[st[0]]
            x = x + 1
        else:
            return 0
    if rstr[len(rstr) - 1] in d.keys():
        tot = tot + d[rstr[len(rstr) - 1]]
    return tot
