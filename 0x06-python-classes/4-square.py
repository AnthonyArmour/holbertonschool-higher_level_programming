#!/usr/bin/python3
"""Private variable size, @property returns size and @size.setter sets size"""


class Square:
    """square is defined by its elements"""
    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        """size is a getter func"""
        return self.__size

    @size.setter
    def size(self, value):
        """is a setter func"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        else:
            if value < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = value

    def area(self):
        """returns square of argument"""
        return self.__size ** 2
