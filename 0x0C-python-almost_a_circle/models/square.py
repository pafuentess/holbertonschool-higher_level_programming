#!/usr/bin/python3


from models.rectangle import Rectangle


class Square(Rectangle):
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)
        self.size = size

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, size):
        self.width = size
        self.height = size

    def __str__(self):
        return "[Square] ({:d}) {:d}/{:d} - {:d}"\
                .format(self.id, self.x, self.y, self.width)

    def update(self, *args, **kwargs):
        if args and len(args) > 0:
            i = 0
            for value in args:
                    if i == 0:
                        self.id = value
                    elif i == 1:
                        self.size = value
                    elif i == 2:
                        self.x = value
                    elif i == 3:
                        self.y = value
                    i += 1
        else:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "size" in kwargs:
                self.size = kwargs["size"]
            if "x" in kwargs:
                self.x = kwargs["x"]
            if "y" in kwargs:
                self.y = kwargs["y"]

    def to_dictionary(self): 
        dic = {}
        dic["id"] = self.id
        dic["size"] = self.size
        dic["x"] = self.x
        dic["y"] = self.y
        return dic
