#!/usr/bin/python3
""" inherits from module """


def inherits_from(obj, a_class):
    """check if an obj inherits directly
    or indirectly from a class

    args:
        obj: variable
        a_class: calss to be checked
    """
    if issubclass(obj, a_class):
        return True
    return False
