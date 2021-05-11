#!/usr/bin/python3
"""class with empty area method"""


class BaseGeometry():
    """class with one empty method"""
    def area(self):
        """empty method"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates value"""
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
        else:
            return True
