#!/usr/bin/python3
"""this is the base class"""

import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns json string representation"""
        if not list_dictionaries or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes json string to a file"""
        lst = str(cls).split("'")
        lst2 = lst[1].split(".")
        json_file = lst2[-1][:] + ".json"
        objs = list()
        d = dict()
        for item in list_objs:
            d = item.to_dictionary()
            objs.append(dict(d))
            d.clear()
        with open(json_file, "w") as fh:
            dump = Base.to_json_string(objs)
            fh.write(dump)
