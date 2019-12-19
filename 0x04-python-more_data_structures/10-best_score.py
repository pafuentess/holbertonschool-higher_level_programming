#!/usr/bin/python3


def best_score(a_dictionary):
    if (a_dictionary):
        b_dictionary = sorted(a_dictionary.items(), key=lambda x: x[1])
        key = sorted(a_dictionary.values())
        for i in a_dictionary:
            if a_dictionary[i] == key[-1]:
                return(i)
        return (i)
    return (None)
