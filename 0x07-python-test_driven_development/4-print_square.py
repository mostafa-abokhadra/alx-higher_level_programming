#!/usr/bin/python3
"""print square module"""


def print_square(size):
    """printing a square of # symbol

        args:
            size: square size
    """
    if type(size) not in [int, float]:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if size < 1 and type(size) is float:
        raise TypeError("size must be an integer")
    size = int(size)
    for i in range(size):
        for j in range(size):
            print("#", end="")
        print("")

    if __name__ == "__main__":
        import doctest
        doctest.testfile("tests/4-print_square.txt")
