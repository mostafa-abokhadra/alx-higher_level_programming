#!/usr/bin/python3

"""anothe square class"""


class Square:
    """suare class the calculate the area
    """
    def __init__(self, size=0):
        """initializing size of squar

        args:
            size: square size
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """calculating the area of the square

        args:
            area: area of the square
        """
        self.area = self.__size ** 2
        return self.area
