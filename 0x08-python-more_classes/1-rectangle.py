#!/usr/bin/python3

"""defining a class based on class"""


class Rectangle:
    """rectangle width and height setter and getter
    """

    def __init__(self, width=0, height=0):
        """ initializing width and height

        args:
            width: the width
            height: the height
        """

        self.__width = width
        self.height = height

    def width(self):
        """return: width"""

        return self.__width

    def width(self, value):
        """ setting the width

        args:
            value: value of setting
        """

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")

    def height(self):
        """ return: the height """

        return self.__height
    def height(self, value):
        """ setting the height

        args:
            value: setting value
        """

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__width = value
