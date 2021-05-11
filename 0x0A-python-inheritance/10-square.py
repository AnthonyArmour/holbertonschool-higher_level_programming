#!/usr/bin/python3
"""square class inherited from rectangle class"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """square class inherited from rectangle class"""
    def __init__(self, size):
        """init method"""
        super(Square, self).__init__(size, size)
        if self.integer_validator("size", size):
            self.__size = size
            self.__height = size
            self.__width = size
