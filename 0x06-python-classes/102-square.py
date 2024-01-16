#!/usr/bin/python3

""" square class """


class Square:
    """ square class, op overloading """

    def __init__(self, size=0):
        """ initializing size

        args:
            size: size of square
        """
        """
        if not isinstance(size, int):
            raise TypeError("size must be a number")
        elif size < 0:
            raise ValueError("size must be >= 0")
        """
        self.__size = size
        self.__area = size ** 2

    @property
    def size(self):
        """ return: the size of sq
        """
        return self.__size

    @size.setter
    def size(self, value):
        """ setting the size

        args:
            value: value of size
        """
        if not isinstance(value, int) or not isinstance(value, float):
            raise TypeError("size must be a number")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.size = value

    @property
    def area(self):
        """ return:the area of square
        """
        return self.size ** 2

    def __eq__(self, sq):
        """ implementing equal equal op

        args:
            sq1: Square(first square)
            sq2: Square(second square)
        """
        if self.area == sq.area:
            return True
        else:
            return False
    def __ne__(self, sq):
        """ implementing not equal op

        args:
            sq1: Square(first square)
            sq2: Square(second square)
        """
        if not self.area == sq.area:
            return True
        else:
            return False

    def __lt__(self, sq):
        """ implementing less than op

        args:
            sq1: Square(first square)
            sq2: Square(second square)
        """
        if self.area < sq.area:
            return True
        else:
            return False

    def __gt__(self, sq):
        """ implementing greater than op

        args:
            sq1: Square(first square)
            sq2: Square(second square)
        """
        if self.area > sq.area:
            return True
        else:
            return False

    def __le__(self, sq):
        """ implementing less than or equal op

        args:
            sq1: Square(first square)
            sq2: Square(second square)
        """
        if self.area <= sq.area:
            return True
        else:
            return False

    def __ge__(self, sq):
        """ implementing greater than or equal op

        args:
            sq1: Square(first square)
            sq2: Square(second square)
        """
        if self.area >= sq.area:
            return True
        else:
            return False
