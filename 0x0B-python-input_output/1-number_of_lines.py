#!/usr/bin/python3


def number_of_lines(filename=""):

    lines = 0
    with open(filename) as fil3:
        for i in fil3:
            lines += 1
    return (lines)
