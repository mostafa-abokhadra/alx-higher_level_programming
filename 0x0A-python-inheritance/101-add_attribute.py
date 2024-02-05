#!/usr/bin/python3
"""adding attributes if possible"""


def add_attribute(obj, name, value):
    """adding attribute to object

    args:
        name: name of it
        value: value of it
    """
    if type(obj).__class__.__module__ == '__builtin':
        raise TypeError("can't add new attribute")
    obj.name = value
