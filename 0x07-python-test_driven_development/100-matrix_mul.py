#!/usr/bin/python3

""" This module contain only one
    function """


def matrix_mul(m_a, m_b):

    """ This function multyply two
        matrix """

    if type(m_a) is not list:
        raise TypeError("m_a must be a list")
    if type(m_b) is not list:
        raise TypeError("m_b must be a list")
    if len(m_a) == 0 or len(m_a[0]) == 0:
        raise ValueError("m_a can't be empty")
    if len(m_b) == 0 or len(m_b[0]) == 0:
        raise ValueError("m_b can't be empty")

    len_m_a = len(m_a)
    len_m_b = len(m_b)
    reference_len_ma = len(m_a[0])
    reference_len_mb = len(m_b[0])
    checklen_ma = 0
    checklen_mb = 0

    for i in m_a:
        if (type(i) is not list):
            raise TypeError("m_a must be a list of lists")

    for j in m_b:
        if (type(j) is not list):
            raise TypeError("m_b must be a list of lists")

    for i in range(0, len(m_a)):
        checklen_ma = len(m_a[i])
        if checklen_ma != reference_len_ma:
            raise TypeError("each row of m_a must be of the same size")
        for j in m_a[i]:
            if (type(j) is not int and type(j) is not float):
                raise TypeError("m_a should contain only integers or floats")

    for i in range(0, len(m_b)):
        checklen_mb = len(m_b[i])
        if checklen_mb != reference_len_mb:
            raise TypeError("each row of m_b must be of the same size")
        for j in m_b[i]:
            if (type(j) is not int and type(j) is not float):
                raise TypeError("m_b should contain only integers or floats")

    if (reference_len_ma != len_m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    new_matrix = []
    matrixrow = []

    for row in m_a:
        matrixrow = []
        column = 0
        while column < reference_len_mb:
            mbcol = list(map(lambda x: x[column], m_b))
            matrixrow.append(sum(list(map(lambda x, y: x * y, row, mbcol))))
            column = column + 1
        new_matrix.append(matrixrow)

    return (new_matrix)
