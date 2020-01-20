#!/usr/bin/python3

""" a class that inherits from int"""


class MyInt(int):
    """ MyInt is a rebel. MyInt has ==
    and != operators inverted """

    def __eq__(self, value):
        return int(self) != value

    def __ne__(self, value):
        return int(self) == value
