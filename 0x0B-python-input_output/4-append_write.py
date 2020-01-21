#!/usr/bin/python3


def append_write(filename="", text=""):

    with open(filename, 'a') as fil3:
        n = fil3.write(text)
    return (n)
