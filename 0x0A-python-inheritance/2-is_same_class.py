#!/usr/bin/python3
""" is same class module """


def is_same_class(obj, a_class):
    """checking if an object is exactly
        a specific type of a class

    args:
        obj: variable
        a_class: class to be checked
    """
    if type(obj) is a_class:
        return True
    return False
