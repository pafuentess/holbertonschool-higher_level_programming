#!/usr/bin/python3
matrix_divided = __import__('2-matrix_divided').matrix_divided

"""
matrix = [
    [1, 2, 3],
    [4, 5, 6]
]


matrix = [
    1,
    [4, 5, 6]
]

matrix = [
    ["hola", 2, 3],
    [4, 5, 6]
]

matrix = 2


matrix = [[1e400, 1e500, 1e600],[1e900, 1e800, 1e700]]
matrix_divided(matrix, 3)
div = 3
"""

#matrix = [[[10.0], [65], [37.0]],[[40], [15.0], [66]]]
#matrix = [[1e100, 1e100],[1e100, 1e100]]
matrix = [[500, 100, 200], [200, 400, 300], [150, 300, 200]]
print(matrix_divided(matrix, 1e500))
print(matrix)
