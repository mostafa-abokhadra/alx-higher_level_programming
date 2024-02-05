#!/usr/bin/python3
""" lookup module """


def lookup(obj):
    """returns:
        list of attributes
    """
    return list(obj.__dict__)
