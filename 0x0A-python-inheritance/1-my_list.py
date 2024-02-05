#!/usr/bin/python3
""" first inheritance class """


class MyList(list):
    """ my list class
    """
    def print_sorted(self):
        if any(not isinstance(i, int) for i in self):
            raise ValueError("only integers allowed")
        """printing a sorted list """
        print(sorted(self))
