#!/usr/bin/python3

"""another square class"""


class Square:
    """adding print method

    attributes:
        size: square size
    """
    def __init__(self, size=0, position=(0, 0)):
        """initialzing size
        """
        self.__size = size
        self.__position = position

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
            for i in range(0, self.__position[1]):
                print()
            for j in range(0, self.__size):
                for k in range(0, self.__position[0]):
                    print(" ", end="")
                    for l in range(0, self.__size):
                        print("#", end="")
                print()
    @property
    def position(self):
        """returns: the position
        """
        return self.__position

    @positon.setter
    def position(self, value):
        """
        """
        if not isinstance(value, tuple) or len(value) < 2:
            pass
        elif not isinstance(value[0], int) or not isinstance(value[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")









