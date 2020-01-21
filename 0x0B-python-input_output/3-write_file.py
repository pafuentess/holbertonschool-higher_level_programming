#!/usr/bin/python3


def write_file(filename="", text=""):

    with open(filename, 'w') as fil3:
        n = fil3.write(text)
    return (n)
