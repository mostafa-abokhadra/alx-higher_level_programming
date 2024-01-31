#!/usr/bin/python3
"""
This is the "Rectangle"  module.

This module provides a simple Rectangle class with attribute width and height.
Default values of both attributes are 0.
"""


class Rectangle:
    """rectangle class
    """

    def __init__(self, width=0, height=0):
        """initializing width and height

        args:
            width: width of rec
            height: height of rec
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        Returns:
            self.width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """setting width

        args:
            value: width of rec
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Returns:
            self.height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """setting height

        args:
            value: height of rec
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

