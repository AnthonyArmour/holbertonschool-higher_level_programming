#!/usr/bin/python3
"""this is the base class"""


class Base():
    """Base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """init method for Base class"""
        if id:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
