#!/usr/bin/python3


def multiple_returns(sentence):
    longsen = len(sentence)
    if (longsen > 0):
        new_tuple = (longsen, sentence[0])
        return (new_tuple)
    else:
        return (None)
