#!/usr/bin/python3

"""anothe square class"""


class Square:
    """square class that add 2 methods to set and get size
    """
    def __init__(self, size=0):
        """initializing size

        args:
            size: size of square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    @property
    def size(self):
        """getting the size
        """
        return self.__size

    @size.setter
    def size(self, value):
        """set size of square

        args:
            value: new size value
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
        
    def area(self):
        """getting the area
        """
        return self.__size ** 2
