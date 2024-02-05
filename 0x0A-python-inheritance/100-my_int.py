#!/usr/bin/python
"""inverting operators modules"""


class MyInt(int):
    """my integer version class"""
    def __init__(self, value):
        """initializing num"""
        if type(value) is not int:
            raise TypeError("must be integer")
        self.__num = value
    def __eq__(self, value):
        """overloading =="""
        if self.__num == value:
            return False
        return True

    def __ne__(self, value):
        """overriding not equal"""
        if self.__num != value:
            return False
        return True

    def __str__(self):
        """str function"""
        return "{}".format(self.__num)
