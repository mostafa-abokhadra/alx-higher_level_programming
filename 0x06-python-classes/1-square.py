#!/usr/bin/python3

"""define class based on class"""


class Square:
    """a square class based on the previous one
    """
    def __init__(self, size=0):
        """intitialize private size

        args:
            size: size of square
        """
        self.__size = size
