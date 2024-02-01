#!/usr/bin/python3
"""say my name module"""


def say_my_name(first_name, last_name=""):
    """printing concatination of first name and last name of a client

        args:
            first_name: 1st name of person
            last_name: last name of person
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    if not first_name:
        raise TypeError("first_name must be a string")
    for char in first_name:
        if not char.isalpha():
            raise TypeError("first_name must be a string")
    for char in last_name:
        if not char.isalpha():
            raise TypeError("last_name must be a string")
    print("My name is {}".format(first_name), end="")
    if last_name:
        print(" {}".format(last_name))
    else:
        print('\n')

    if __name__ == "__main__":
        import doctest
        doctest.testfile("tests/3-say_my_name.txt")
