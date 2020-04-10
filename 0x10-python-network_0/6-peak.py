#!/usr/bin/python3
""" doc """


def find_peak(list_of_integers):
    """ doc """
    if list_of_integers:
        list_of_integers.sort()
        return (list_of_integers[-1])
