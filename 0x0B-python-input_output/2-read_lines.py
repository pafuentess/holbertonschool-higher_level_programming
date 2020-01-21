#!/usr/bin/python3


def number_of_lines(filename=""):

    lines = 0
    with open(filename) as fil3:
        for i in fil3:
            lines += 1
    return (lines)


def read_lines(filename="", nb_lines=0):

    count = 0
    with open(filename) as fil3:
        number_lines = number_of_lines(filename)
        if (nb_lines <= 0 or nb_lines >= number_lines):
            print(fil3.read(), end='')
        else:
            for i in fil3:
                count += 1
                if (count <= nb_lines):
                    string = str(i)
                    print(string, end='')
                else:
                    break
