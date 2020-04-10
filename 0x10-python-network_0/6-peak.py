#!/usr/bin/python3
""" doc """


def find_peak(list_of_integers):
    """ doc """
    aux = 0
    if list_of_integers:
        lenght = len(list_of_integers)
        for i in range(1, lenght - 1):
            if list_of_integers[i] > list_of_integers[i - 1] and\
                    list_of_integers[i] > list_of_integers[i + 1]:
                        return (list_of_integers[i])
            elif list_of_integers[i - 1] and\
                    list_of_integers[i] == list_of_integers[i - 1] and\
                    list_of_integers[i + 1] and\
                    list_of_integers[i] == list_of_integers[i + 1]:
                    return (list_of_integers[i])
    else:
        return (None)
