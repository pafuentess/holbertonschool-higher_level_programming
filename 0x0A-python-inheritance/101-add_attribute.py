#!/usr/bin/python3

""" this module has one function"""


def add_attribute(obj, name, value):

    """ function to add atributes """

    if (hasattr(obj, '__dict__') is False):
        raise TypeError("can't add new attribute")
    else:
        setattr(obj, name, value)
