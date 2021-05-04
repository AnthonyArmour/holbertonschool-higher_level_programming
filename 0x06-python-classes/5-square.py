#!/usr/bin/python3
"""Private variable size, @property returns size and @size.setter sets size"""


class Square:
    """square is defined by its elements"""
    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        """is getter func"""
        return self.__size

    @size.setter
    def size(self, value):
        """is setter func"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        else:
            if value < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = value

    def area(self):
        """return square of an argument"""
        return self.__size ** 2

    def my_print(self):
        """prints square of #'s that is determined by size"""
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                for n in range(self.__size):
                    print("{}".format("#"), end="")
                print()
