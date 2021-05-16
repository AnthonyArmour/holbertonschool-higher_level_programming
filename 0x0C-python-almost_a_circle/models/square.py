#!/usr/bin/python3
"""Square class inherits from Rectangle class"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class inherits from Rectangle class"""
    def __init__(self, size, x=0, y=0, id=None):
        """init method for square class"""
        super().__init__(size, size, x, y, id)
        self.size = size

    @property
    def size(self):
        """size getter method"""
        return self.__width

    @size.setter
    def size(self, value):
        """size setter"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value
            self.__height = value

    def __str__(self):
        """return printablbe instance"""
        return ("[Square] (" + str(self.id) + ") " + str(self.x) + "/" +
                str(self.y) + " - " + str(self.size))

    def update(self, *args, **kwargs):
        """updates attruibutes"""
        if len(args) == 0 or args == []:
            for k, v in kwargs.items():
                setattr(self, k, v)
            return
        else:
            lst = ["id", "size", "x", "y"]
            for n in range(len(args)):
                setattr(self, lst[n], args[n])

    def to_dictionary(self):
        """returns dictionary of instance attributes"""
        d = dict()
        lst = ["id", "size", "x", "y"]
        for n in lst:
            d[n] = getattr(self, n)
        return d
