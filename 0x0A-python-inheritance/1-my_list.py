#!/usr/bin/python3
""" first inheritance class """


class MyList(list):
    """ my list class
    """
    def print_sorted(self):
        """printing a sorted list """
        print(sorted(self))
