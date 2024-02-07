#!/usr/bin/python3
"""append module"""


def append_write(filename="", text=""):
    """appending to a file

    args:
        filename: the file to append to
        text: text to append to the file
    """
    with open(filename, mode='a', encoding='utf-8') as fily:
        return fily.write(text)
