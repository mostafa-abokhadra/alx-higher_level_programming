#!/usr/bin/python3
"""adding two numbers module"""


def add_integer(a, b=98):
    """adding two integers

    args:
        a: first number
        b: second number

    Returns:
        sum of a and b
    """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)
    return a + b

    if __name__ == "__main__":
        import doctest
        doctest.testfile("tests/0-add_integer.txt")
