#!/usr/bin/python3
"""class to json module"""


def class_to_json(obj):
    """class to json

    args:
        obj: object to convert
    """
    return obj.__dict__
