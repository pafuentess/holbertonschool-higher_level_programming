#!/usr/bin/python3


def uniq_add(my_list=[]):
    no_repeat = []
    suma = 0
    for i in my_list:
        if i not in no_repeat:
            no_repeat.append(i)

    for i in no_repeat:
        suma = suma + i

    return (suma)
