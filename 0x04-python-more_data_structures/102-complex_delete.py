#!/usr/bin/python3


def complex_delete(a_dictionary, value):
    to_remove = []
    for i in a_dictionary:
        if a_dictionary[i] == value:
            to_remove.append(i)
    for j in to_remove:
        del a_dictionary[j]
    return (a_dictionary)
