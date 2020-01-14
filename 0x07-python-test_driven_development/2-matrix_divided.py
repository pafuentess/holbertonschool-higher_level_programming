#!/usr/bin/python3

""" This module only contain one function"""


def matrix_divided(matrix, div):

    """ matrix: a list of list, an eache element
        are divided by div.
        return the matrix with the new elements value """

    if type(matrix) is not list or len(matrix) == 0:
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")

    if (type(matrix[0]) is not list):
            raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats")
    referencelen = len(matrix[0])
    checklen = 0
    flag = 0
    error = "matrix must be a matrix (list of lists) of integers/floats"

    if div == 0:
        raise ZeroDivisionError("division by zero")
    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")

    for i in range(0, len(matrix)):
        if (type(matrix[i]) is not list):
            raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats")
        checklen = len(matrix[i])
        if checklen != referencelen:
            raise TypeError("Each row of the matrix must have the same size")
        for j in matrix[i]:
            if (type(j) is not int and type(j) is not float):
                raise TypeError(error)

    return (list(map(lambda row: list(map(
        lambda col: round(col / div, 2), row)), matrix)))
