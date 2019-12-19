#!/usr/bin/python3


def roman_to_int(roman_string):
    if (roman_string):
        r = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        suma = 0
        for i in roman_string:
            suma = suma + r[i]
        return suma
    return (0)
