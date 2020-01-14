#!/usr/bin/python3

""" This module only have one
    function; add two integer """


def add_integer(a, b=98):

    """ a and b arguments to add,
        return a + b """

    if a != a:
        return float('NaN')
    if b != b:
        return float('NaN')
    if a is None:
        raise TypeError("a must be an integer")
    if (type(a) is not int and type(a) is not float):
        raise TypeError("a must be an integer")
    if (type(b) is not int and type(b) is not float):
        raise TypeError("b must be an integer")
    if ((a + b) == float('inf')):
        return (None)
    if ((a + b) == -float('inf')):
        return (None)
    if (type(a) is float):
        a = int(a)
    if (type(b) is float):
        b = int(b)

    return(a + b)
