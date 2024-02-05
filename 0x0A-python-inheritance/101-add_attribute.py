#!/usr/bin/python3
"""adding attributes if possible"""


def add_attribute(obj, name, value):
    if type(obj).__class__.__module__ == '__builtin':
        raise TypeError("can't add new attribute")
    obj.name = value
