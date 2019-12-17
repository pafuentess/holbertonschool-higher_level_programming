#!/usr/bin/python3


def add_tuple(tuple_a=(), tuple_b=()):

    longt1 = len(tuple_a)
    longt2 = len(tuple_b)

    if (longt1 == 0):
        tuple_a = 0, 0
    if (longt1 == 1):
        tuple_a = tuple_a[0], 0
    if (longt2 == 0):
        tuple_b = 0, 0
    if (longt2 == 1):
        tuple_b = tuple_b[0], 0

    new_tuple = ((tuple_a[0] + tuple_b[0]), (tuple_a[1] + tuple_b[1]))

    return (new_tuple)
