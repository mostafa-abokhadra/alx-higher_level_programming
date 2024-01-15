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
    def size(self):
        """ getting size

        Return: size
        """
        return self.__size

    @size.setter
    def size(self, value):
        """ setting size appropriately

        args:
            size: size of square
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """ calculating the area of a square

        Return: area of square
        """
        return self.__size ** 2

    def my_print(self):
        """ printing the suare using #
        """
        if self.__size == 0:
            print()
        else:
            for i in range(0, self.__size):
                for j in range (0, self.__size):
                    print("#", end="")
                print()
