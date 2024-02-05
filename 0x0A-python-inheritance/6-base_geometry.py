#!/usr/bin/python3
""" module of gometry """


class BaseGeometry:
    """ class that not define an area :) """
    def area(self):
        """raising an exception of not defined area
        """
        raise Exception("area() is not implemented")
