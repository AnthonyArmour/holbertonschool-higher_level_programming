#!/usr/bin/python3
"""class with empty area method"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """rectangle class inherited from BaseGeometry"""
    def __init__(self, width, height):
        """init method"""
        super().__init__()
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
