#!/usr/bin/python3


def print_list_integer(my_list=[]):
    longi = len(my_list)
    for i in range(longi):
        print("{:d}".format(my_list[i]))
