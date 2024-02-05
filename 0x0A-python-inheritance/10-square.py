#!/usr/bin/python3
"""square module"""


"""importing rectangle module"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """squar that inherits from rectangle"""
    def __init__(self, size):
        """initialize size
        
        args:
            size: size of square
        """
        super().integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """returns:
            area of a square
        """
        return self.__size * self.__size
