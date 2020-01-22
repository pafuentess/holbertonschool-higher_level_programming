#!/usr/bin/python3


def pascal_triangle(n):

    triangle = [[1]]
    new = []
    lenght = 0
    if n <= 0:
        return (new)

    for row in range(0, n-1):
        lenght = len(triangle[row])
        for element in range(lenght + 1):
            if element == 0 or element == lenght:
                new.append(1)
            else:
                new.append(triangle[row][element - 1] + triangle[row][element])
        copy_row = new[:]
        triangle.append(copy_row)
        new.clear()
    return (triangle)
