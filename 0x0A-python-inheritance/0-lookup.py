#!/usr/bin/python3
""" lookup module """


def lookup(obj):
    """returns:
        list of attributes
    """
    return obj.__dict__
