#!/usr/bin/python3
"""myint has inverted eq"""


class MyInt(int):
    """myint has eq inverted"""
    def __init__(self, num):
        """init int"""
        int.__init__(self)
        self.num = num

    def __eq__(self, other):
        """inverted eq"""
        return int(self.num) != other

    def __ne__(self, other):
        """inverted ne"""
        return not self.__eq__(other)
