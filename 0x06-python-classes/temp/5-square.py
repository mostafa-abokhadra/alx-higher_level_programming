#!/usr/bin/python3

"""another square class"""


class Square:
    """adding print method

    attributes:
        size: square size
    """
    def __init__(self, size=0):
        """initialzing size
        """
        self.__size = size

    @property
    def size(self):
        """returns: the size
        """
        return self.__size

    @size.setter
    def size(self, value):
        """setting the size of the square

        args:
            value: new size
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """returns: the area
        """
        return self.__size ** 2

    def my_print(self):
        """printing to stdout the square it self using # symbol
        """
        if self.__size == 0:
            print()
        else:
            for j in range(0, self.__size):
                for i in range(0, self.__size):
                    print("#", end="")
                print()
