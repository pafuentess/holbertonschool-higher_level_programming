#!/usr/bin/python3


def weight_average(my_list=[]):
    if (my_list):
        sumap = 0
        sumad = 0
        result = 0
        for tupla in my_list:
            sumap = sumap + (tupla[0] * tupla[1])
            sumad = sumad + tupla[1]

        result = sumap / sumad
        return (result)
    return (0)
