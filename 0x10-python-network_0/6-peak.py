#!/usr/bin/python3
""" finding a peak module """


def find_peak(list_of_integers):
    """finding a peak
    """
    if not list_of_integers:
        return None
    return max(list_of_integers)
