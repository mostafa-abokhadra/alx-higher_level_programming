#!/usr/bin/python3

""" class to add some errors """


class Square:
    """ adding some features
    """
    def __init__(self, size=0):
        """ initializing size

        args:
            size: size of square
        """
        self.__size = size

    @property
    def get_size(self):
        """ getting size

        Return: size
        """
        return self.__size

    def set_size(self, size):
        """ setting size appropriately

        args:
            size: size of square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
