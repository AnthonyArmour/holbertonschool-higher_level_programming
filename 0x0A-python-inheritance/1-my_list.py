#!/usr/bin/python3
"""inherits from list"""


class MyList(list):
    """inherits from type list"""

    def __init__(self):
        """init method"""
        list.__init__(self)

    def __getitem__(self, key):
        """init for mylist"""
        return list.__getitem__(self, key-1)

    def __setitem__(self, key, item):
        """sets item"""
        self[key-1] = item

    def print_sorted(self):
        """returns a sorted list in ascending order"""
        lst = list()
        for n in self:
            if len(lst) < 1:
                lst.append(n)
                continue
            for x in range(len(lst)):
                if n <= lst[x]:
                    lst.insert(x, n)
                    break
                if x == len(lst) - 1:
                    lst.append(n)
        print("{}".format(lst))
