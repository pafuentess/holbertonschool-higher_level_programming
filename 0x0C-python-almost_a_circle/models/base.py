#!/usr/bin/python3

""" module base """

import json


class Base:
    """ class base """
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ method 1 """

        if list_dictionaries is None or len(list_dictionaries) == 0:
            return ([])
        else:
            return(json.dumps(list_dictionaries))

    @classmethod
    def save_to_file(cls, list_objs):
        """ method 2 """
        filename = cls.__name__ + ".json"
        dic = []
        if list_objs is not None:
            for element in list_objs:
                dic.append(cls.to_dictionary(element))
        with open(filename, 'w') as fil3:
            fil3.write(cls.to_json_string(dic))

    @staticmethod
    def from_json_string(json_string):
        """ method 3 """
        if json_string is None or len(json_string) == 0:
            return ([])
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ method 4 """
        if cls.__name__ is "Rectangle":
            dumy = cls(1, 1)
        elif cls.__name__ is "Square":
            dumy = cls(1)
        dumy.update(**dictionary)
        return dumy

    @classmethod
    def load_from_file(cls):
        """ method 5 """
        filename = cls.__name__ + ".json"
        instances = []
        try:
            with open(filename, 'r') as fil3:
                lisst = cls.from_json_string(fil3.read())
                for dic in lisst:
                    instances.append(cls.create(**dic))
                return instances
        except Exception:
            return instances
