#!/usr/bin/python3
"""Rectangle class"""


from models.base import Base


class Rectangle(Base):
    """Rectangle class"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """rectangle init method"""
        super().__init__(id)
        if type(width) is not int:
            raise TypeError("width must be an integer")
        elif width <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = width
        if type(height) is not int:
            raise TypeError("height must be an integer")
        elif height <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = height
        if type(x) is not int:
            raise TypeError("x must be an integer")
        elif x < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = x
        if type(y) is not int:
            raise TypeError("y must be an integer")
        elif y < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = y

    @property
    def width(self):
        """getter func"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter method for width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value

    @property
    def height(self):
        """getter method for height"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter method for height"""
        if type(value) is int:
            if value <= 0:
                raise ValueError("height must be > 0")
            else:
                self.__height = value
        else:
            raise TypeError("height must be an integer")

    @property
    def x(self):
        """setter method for x"""
        return self.__x

    @x.setter
    def x(self, value):
        """setter method for x"""
        if type(value) is int:
            if value < 0:
                raise ValueError("x must be >= 0")
            else:
                self.__x = value
        else:
            raise TypeError("x must be an integer")

    @property
    def y(self):
        """getter method for y"""
        return self.__y

    @y.setter
    def y(self, value):
        """setter method for y"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = value

    def area(self):
        """returns area"""
        return self.__width * self.__height

    def display(self):
        """displays rectangle with #"""
        if self.__y > 0:
            print("{}".format("\n" * self.__y), end="")
        for n in range(self.__height):
            if self.__x > 0:
                print("{}".format(" " * self.__x), end="")
            print("{}\n".format("#" * self.__width), end="")

    def __str__(self):
        """printable params"""
        return ("[Rectangle] (" + str(self.id) + ") " + str(self.__x) + "/" +
                str(self.__y) + " - " + str(self.__width) + "/" +
                str(self.__height))

    def update(self, *args, **kwargs):
        """updates instance"""
        if len(args) == 0 or args == []:
            for k, v in kwargs.items():
                setattr(self, k, v)
            return
        x = 0
        lst = ["id", "width", "height", "x", "y"]
        for n in range(len(args)):
            setattr(self, lst[x], int(args[n]))
            x += 1

    def to_dictionary(self):
        """returns dictionary of attributes"""
        d = dict()
        lst = ["id", "width", "height", "x", "y"]
        for n in lst:
            d[n] = getattr(self, n)
        return d
