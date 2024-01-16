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
        if not isinstance(position, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif not len(position) == 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif not isinstance(position[0], int) or not isinstance(position[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif position[0] < 0 or position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = position

    @property
    def size(self):
        """returns: the size
        """
        return self.__size

    @property
    def position(self):
        """returns: the position
        """
        return self.__position

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

    @position.setter
    def position(self, value):
        """ setting positon of square

        args:
            value: value of pos
        """
        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif not len(value) == 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif not isinstance(value[0], int) or not isinstance(value[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

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
            for s in range(0, self.__position[1]):
                print()
            for j in range(0, self.__size):
                for k in range(0, self.__position[0]):
                    print(" ", end="")
                for i in range(0, self.__size):
                    print("#", end="")
                print()


