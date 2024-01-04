#!/usr/bin/python3

"""defining a class based on class"""


class Rectangle:
    """Rectangle class

    Attributes:
        width: rec wid
        height: rec height

    """

    def __init__(self, width=0, height=0):
        """initializing width and height

        Args:
            width: the width
            height: the height

        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Returns:
                width
        """
        return self.__width
    
    @width.setter
    def width(self, value):
        """setting the width

        Args:
            value: value of setting

        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value
    
    @property
    def height(self):
        """ Returns:
                the height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """ setting the height

        Args:
            value: setting value
        """

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
