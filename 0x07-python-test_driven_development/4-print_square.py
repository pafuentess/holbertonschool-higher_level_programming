#!/usr/bin/python3

""" This module only contain one function """


def print_square(size):

    """ print a square according the size """

    if (type(size) is not int):
        raise TypeError("size must be an integer")
    if (size < 0):
        raise ValueError("size must be >= 0")
    if (type(size) is float and size < 0):
        raise TypeError("size must be an integer")

    for i in range(0, size):
        for j in range(0, size):
            print("#", end="")
        print()
