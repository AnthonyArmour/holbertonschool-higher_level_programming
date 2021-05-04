#!/usr/bin/python3
"""Private variable size, @property returns size and @size.setter sets size"""


class Square:
    """square defined by its elements"""
    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.position = position

    @property
    def size(self):
        """getter func"""
        return self.__size

    @size.setter
    def size(self, value):
        """setter func"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        else:
            if value < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = value

    @property
    def position(self):
        """getter func"""
        return self.__position

    @position.setter
    def position(self, value):
        """setter func"""
        if len(value) < 2 or type(value) is not tuple:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif type(value[1]) is not int or type(value[0]) is not int:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """returns square of argument"""
        return self.__size ** 2

    def my_print(self):
        """prints square of #'s size of size squared"""
        if self.__size > 0:
            print("{}".format('\n' * self.__position[1]), end='')
            for i in range(self.__size):
                for t in range(self.__position[0]):
                    print("{}".format(" "), end="")
                for n in range(self.__size):
                    print("{}".format("#"), end="")
                print()
        else:
            print()
