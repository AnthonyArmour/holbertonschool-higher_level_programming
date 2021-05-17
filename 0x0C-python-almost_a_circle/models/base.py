#!/usr/bin/python3
"""this is the base class"""

import json
import csv


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
        json_file = cls.__name__ + ".json"
        objs = list()
        d = dict()
        if list_objs:
            for item in list_objs:
                d = item.to_dictionary()
                objs.append(dict(d))
                d.clear()
        with open(json_file, "w+") as fh:
            if list_objs is None:
                fh.write("[]")
                return
            dump = Base.to_json_string(objs)
            fh.write(dump)

    @staticmethod
    def from_json_string(json_string):
        """returns json list from json string"""
        if not json_string or json_string == []:
            return list()
        st = ""
        lst = list()
        n = 1
        while n < len(json_string) - 1:
            st = st + json_string[n]
            if json_string[n] == "}":
                lst.append(json.loads(st))
                st = ""
                n += 2
            n += 1
        return lst

    @classmethod
    def create(cls, **dictionary):
        """creates instance"""
        if "size" in dictionary.keys():
            instance = cls(1)
        if "height" in dictionary.keys():
            instance = cls(1, 1)
        instance.update(**dictionary)
        return instance

    @classmethod
    def load_from_file(cls):
        """returns list of created instances"""
        json_file = cls.__name__ + ".json"
        instances = list()
        try:
            with open(json_file, "r") as fh:
                text = fh.read()
                objs = Base.from_json_string(text)
                for d in objs:
                    temp = cls.create(**d)
                    instances.append(temp)
            return instances
        except:
            return list()

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """saves csv formatted obj to file"""
        csv_file = cls.__name__ + ".csv"
        if cls.__name__ == "Rectangle":
            field = ['id', 'width', 'height', 'x', 'y']
        else:
            field = ['id', 'size', 'x', 'y']
        lst = list()
        with open(csv_file, "w") as fh:
            if list_objs:
                writer = csv.DictWriter(fh, fieldnames=field)
                writer.writeheader()
                for items in list_objs:
                    d = items.to_dictionary()
                    lst.append(dict(d))
                    d.clear()
                writer.writerows(lst)
            else:
                fh.write("")

    @classmethod
    def load_from_file_csv(cls):
        """loads from csv file"""
        csv_file = cls.__name__ + ".csv"
        lst = list()
        try:
            with open(csv_file, "r") as fh:
                reader = csv.DictReader(fh)
                res = list(reader)
                for d in res:
                    for item in d.keys():
                        d[item] = int(d[item])
                    temp = cls.create(**d)
                    lst.append(temp)
            return lst
        except:
            return list()
