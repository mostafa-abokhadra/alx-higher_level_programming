#!/usr/bin/python3
"""square module"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """sqaur class that inherits from rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)
        self.size = size

    def __str__(self):
        return "[Square] ({}) {}/{} - {}".format(
                self.id, self.x, self.y, self.size)

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        super().errors("size", size)
        self.__width = size
        self.__height = size
        self.__size = size

    def update(self, *args, **kwargs):
        if args:
            for i in range(len(args)):
                if i == 1:
                    for j in range(1, 4):
                        if j == 3:
                            setattr(self, Rectangle.attrs[-1], args[i])
                        setattr(self, Rectangle.attrs[j], args[i])
                    continue
                setattr(self, Rectangle.attrs[i], args[i])
        else:
            for key in kwargs:
                setattr(self, key, kwargs[key])
