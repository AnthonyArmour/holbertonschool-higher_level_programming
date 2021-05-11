#!/usr/bin/python3
"""class with empty area method"""


class BaseGeometry():
    """class with one empty method"""
    def __init__(self):
        """empty init method"""
        pass

    def area(self):
        """empty method"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates value"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
        else:
            return True


class Rectangle(BaseGeometry):
    """rectangle class inherited from BaseGeometry"""
    def __init__(self, width, height):
        """init method"""
        super(Rectangle, self).__init__()
        try:
            self.integer_validator("width", width)
        except Exception as e:
            print("[{}] {}".format(e.__class__.__name__, e))
        else:
            self.__width = width
        try:
            self.integer_validator("height", height)
        except Exception as e:
            print("[{}] {}".format(e.__class__.__name__, e))
        else:
            self.__height = height
