#!/usr/bin/python3

""" a module with one class """


class MyList(list):
    """ print a sorted list"""
    def print_sorted(self):
        print(sorted(self))
