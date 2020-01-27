#!/usr/bin/python3

""" module rectangle """

from models.base import Base


class Rectangle(Base):
    """ class rectangle """

    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """ method 1 """
        return self.__width

    @width.setter
    """ method 2 """
    def width(self, width):
        if (type(width) is not int):
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @property
    def height(self):
        """ method 3 """
        return self.__height

    @height.setter
    def height(self, height):
        """ method 4 """
        if (type(height) is not int):
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @property
    def x(self):
        """ method 5 """
        return self.__x

    @x.setter
    def x(self, x):
        """method 6"""
        if (type(x) is not int):
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @property
    def y(self):
        """ method 7 """
        return self.__y

    @y.setter
    def y(self, y):
        """ method 8 """
        if (type(y) is not int):
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        """ method 9 """
        return (self.__height * self.__width)

    def display(self):
        """ method 10 """
        for i in range(0, self.__y):
            print()
        for i in range(0, self.__height):
            for j in range(0, (self.__width + self.__x)):
                if j < self.__x:
                    print(" ", end='')
                else:
                    print("#", end='')
            print()

    def __str__(self):
        """ method 11 """
        return ("[Rectangle] ({:d}) {:d}/{:d} - {:d}/{:d}".format
                (self.id, self.__x, self.__y, self.__width, self.__height))

    def update(self, *args, **kwargs):
        """ method 12 """
        if args and len(args) > 0:
            i = 0
            for value in args:
                    if i == 0:
                        self.id = value
                    elif i == 1:
                        self.width = value
                    elif i == 2:
                        self.height = value
                    elif i == 3:
                        self.x = value
                    elif i == 4:
                        self.y = value
                    i += 1
        else:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "width" in kwargs:
                self.width = kwargs["width"]
            if "height" in kwargs:
                self.height = kwargs["height"]
            if "x" in kwargs:
                self.x = kwargs["x"]
            if "y" in kwargs:
                self.y = kwargs["y"]

    def to_dictionary(self):
        """method 13 """
        dic = {}
        dic["id"] = self.id
        dic["width"] = self.width
        dic["height"] = self.height
        dic["x"] = self.x
        dic["y"] = self.y
        return dic
