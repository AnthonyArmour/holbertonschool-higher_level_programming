#!/usr/bin/python3
"""square class inherited from rectangle class"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """square class inherited from rectangle class"""
    def __init__(self, size):
        """init method"""
        if super().integer_validator("size", size):
            super(Square, self).__init__(size, size)
            self.__size = size
            self.__width = size
            self.__height = size

    def area(self):
        """area of square"""
        return (self.__size * self.__size)

    def __str__(self):
        """prints square discription"""
        return "[Square] " + str(self.__size) + "/" + str(self.__size)
