#!/usr/bin/python3
""" module of gometry """


class BaseGeometry:
    """ class that not define an area :) """
    def area(self):
        """raising an exception of not defined area
        """
        raise Exception("area() is not implemented")


    def integer_validator(self, name, value):
        """integer validate

        args:
            name: value key
            value: value of key
        """
        if not type(name) == str:
            raise TypeError("name must be a string")
        if not type(name) == int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
