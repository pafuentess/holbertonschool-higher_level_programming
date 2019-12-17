#!/usr/bin/python3


def element_at(my_list, idx):
    if (idx < 0):
        return (None)
    longi = len(my_list)
    if (idx > longi):
        return (None)
    return (my_list[idx])
