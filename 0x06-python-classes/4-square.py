#!/usr/bin/python3

"""anothe square class"""


class Square:
    """
    square class that add 2 methods to set and get size

    attributes:
        size: square size
    """
    def __init__(self, size=0):
        """initializing size

        args:
            size: size of square
        """
        self.__size = size

    @property
    def size(self):
        """returns: the size
        """
        return self.__size

    @size.setter
    def size(self, value):
        """property setter for size

        args:
            value(int): new size value

        raises:
            TypeError: size must be an integer
            ValueError: size must be >= 0
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
        
    def area(self):
        """getting the area

        returns: the area
        """
        return self.__size ** 2
