#!/usr/bin/python3
"""student class"""


class Student():
    """student class"""
    def __init__(self, first_name, last_name, age):
        """init method"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """returns dictionary description of class obj"""
        if attrs is None:
            return self.__dict__
        d = dict()
        for item in attrs:
            try:
                d[item] = getattr(self, item)
            except:
                continue
        return d

    def reload_from_json(self, json):
        """replaces all attributes of instance"""
        if json != {}:
            self.first_name = json["first_name"]
            self.last_name = json["last_name"]
            self.age = json["age"]
