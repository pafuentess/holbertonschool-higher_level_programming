#!/usr/bin/python3


def print_reversed_list_integer(my_list=[]):
    longi = len(my_list)
    for i in range(longi - 1, -1, -1):
        print(my_list[i])