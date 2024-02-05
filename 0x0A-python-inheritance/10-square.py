#!/usr/bin/python3
""" square module """

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square that inherits from Rectangle"""
    def __init__(self, size):
        """initialize the size"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """square area"""
        return self.__size ** 2
