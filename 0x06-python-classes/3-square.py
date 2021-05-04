#!/usr/bin/python3
"""Square has private variable size"""


class Square:
    """Square init size to 0 if type int"""
    def __init__(self, size=0):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        else:
            if size < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = size

    def area(self):
        """returns square of argument"""
        return self.__size ** 2
