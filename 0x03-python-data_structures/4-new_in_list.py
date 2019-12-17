#!/usr/bin/python3


def new_in_list(my_list, idx, element):
    if (idx < 0):
        return (my_list)

    longi = len(my_list)
    if (idx > longi):
        return (my_list)

    cpy_list = my_list[:]
    cpy_list[idx] = element

    return (cpy_list)
