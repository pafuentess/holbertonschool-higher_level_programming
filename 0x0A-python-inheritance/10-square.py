#!/usr/bin/python3

""" this is a subclass of the class rectangle """

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):

    """ subclass rectangle """

    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        return self.__size * self.__size
