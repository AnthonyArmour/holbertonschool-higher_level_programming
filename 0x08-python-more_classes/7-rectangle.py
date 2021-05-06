#!/usr/bin/python3
"""Defines a rectangle"""


class Rectangle:
    """Rectangle Class"""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """this is an init method"""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """getter func"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter func"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """getter func for height"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter func for height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """finds area of rectangle"""
        return self.__height * self.__width

    def perimeter(self):
        """finds perimeter of rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return ((self.__height * 2) + (self.__width * 2))

    def __str__(self):
        """makes printable rectangle from #"""
        st = ""
        if self.__width != 0 and self.__height != 0:
            for x in range(self.__height):
                st = st + (str(self.print_symbol) * self.__width) + "\n"
            return st[:len(st) - 1]
        else:
            return ""

    def __repr__(self):
        """makes printable rectangle from #"""
        st = "Rectangle("
        return st + str(self.__width) + ", " + str(self.__height) + ")"

    def __del__(self):
        """del message method"""
        print("{}".format("Bye rectangle..."))
        if Rectangle.number_of_instances > 0:
            Rectangle.number_of_instances -= 1
