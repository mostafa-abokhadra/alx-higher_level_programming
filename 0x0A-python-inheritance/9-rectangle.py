#!/usr/bin/python3
""" base class module """


""" base geometry class module """
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """inheriting class"""
    def __init__(self, width, height):
        """initializing vars

        args:
            width: width of rec
            height: height of rec
        """
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """returns:
            area of rec
        """
        return self.__width * self.__height

    def __str__(self):
        """ str fucntion """
        return "[Rectangle] {}/{}".format(
                self.__width, self.__height)
