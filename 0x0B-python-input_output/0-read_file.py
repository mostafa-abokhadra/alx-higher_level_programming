#!/usr/bin/python3
"""reading from file"""


def read_file(filename=""):
    """reading a file

    args:
        filename: the file to be read
    """
    with open(filename, mode='r', encoding='utf-8') as fily:
        print(fily.read(), end='')
