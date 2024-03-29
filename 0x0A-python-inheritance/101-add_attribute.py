#!/usr/bin/python3
"""adding attributes if possible"""


def add_attribute(obj, name, value):
    """adding attribute to object

    args:
        name: name of it
        value: value of it
    """
    if not hasattr(obj, '__dict__'):
        raise TypeError("can't add new attribute")
    setattr(obj, name, value)
