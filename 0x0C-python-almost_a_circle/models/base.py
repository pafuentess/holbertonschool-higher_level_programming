#!/usr/bin/python3

import json


class Base:
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return ([])
        else:
            return(json.dumps(list_dictionaries))

    @classmethod
    def save_to_file(cls, list_objs):
        filename = cls.__name__ + ".json"
        dic = []
        if list_objs is not None:
            for element in list_objs:
                dic.append(cls.to_dictionary(element))
        with open(filename, 'w') as fil3:
            fil3.write(cls.to_json_string(dic))
