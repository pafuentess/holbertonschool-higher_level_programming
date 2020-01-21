#!/usr/bin/python3

""" this file contains one class"""


class Student:

    """ the student class """

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if attrs is None:
            return self.__dict__

        store_values = {}
        for i in attrs:
            if i in self.__dict__.keys():
                store_values[i] = self.__dict__[i]
        return (store_values)
