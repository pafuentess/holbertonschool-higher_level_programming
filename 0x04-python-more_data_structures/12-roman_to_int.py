#!/usr/bin/python3


def roman_to_int(roman_string):
    if (type(roman_string) is not str):
        return (0)
    if (roman_string == ""):
        return (0)
    r = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    suma = 0
    check = 0
    for i in roman_string:
        check = r.get(i)
        if check:
            suma = suma + r[i]
        else:
            return (0)
    return (suma)
