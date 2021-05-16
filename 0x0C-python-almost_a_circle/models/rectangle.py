#!/usr/bin/python3
"""Rectangle class"""


from models.base import Base


class Rectangle(Base):
    """Rectangle class"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """rectangle init method"""
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """getter func"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter method for width"""
        self.__width = value

    @property
    def height(self):
        """getter method for height"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter method for height"""
        self.__height = value

    @property
    def x(self):
        """setter method for x"""
        return self.__x

    @x.setter
    def x(self, value):
        """setter method for x"""
        self.__x = value

    @property
    def y(self):
        """getter method for y"""
        return self.__y

    @y.setter
    def y(self, value):
        """setter method for y"""
        self.__y = value
