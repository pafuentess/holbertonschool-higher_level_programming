#!/usr/bin/python3

""" This module contain only one function """


def text_indentation(text):

    """ Separate the string by . : ? """

    if type(text) is not str:
        raise TypeError("text must be a string")

    i = 0
    leng = len(text)
    flag = 0

    for i in text:

        if flag == 0:
            if i == " ":
                continue
            else:
                flag = 1

        if flag == 1:
            if i == "." or i == "?" or i == ":":
                print(i)
                print()
                flag = 0
            else:
                print(i, end='')
