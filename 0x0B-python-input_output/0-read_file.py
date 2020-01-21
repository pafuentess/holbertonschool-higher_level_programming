#!/usr/bin/python3


def read_file(filename=""):

    with open(filename, 'r') as fil3:
        print(fil3.read(), end='')
