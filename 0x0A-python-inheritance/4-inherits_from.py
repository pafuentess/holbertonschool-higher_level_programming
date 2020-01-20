#!/usr/bin/python3

""" this file contains one function """


def inherits_from(obj, a_class):

    """ object is an instance of a class that
    inherited (directly or indirectly)
    from the specified class """

    if (type(obj) is not a_class):
        return (issubclass(type(obj), a_class))
    else:
        return (False)
