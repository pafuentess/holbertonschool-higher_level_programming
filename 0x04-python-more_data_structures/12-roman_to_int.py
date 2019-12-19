#!/usr/bin/python3


def roman_to_int(roman_string):

    if (type(roman_string) is not str):
        return (0)
    if (roman_string == ""):
        return (0)

    r = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

    suma = 0
    prev = 0
    check = 0

    for i in roman_string:
        check = r.get(i, 0)
        if (check > prev):
            suma = suma - (2 * prev)
            suma = suma + check
        else:
            suma = suma + check
        prev = check

    return (suma)
