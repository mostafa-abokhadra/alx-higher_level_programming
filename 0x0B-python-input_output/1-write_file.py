#!/usr/bin/python3
"""write to file module"""


def write_file(filename="", text=""):
    """writing to file

    args:
        filename: pointer to a file to write in
        text: text to write into the file
    """
    with open(filename, mode='w', encoding='utf-8') as fily:
        return fily.write(text)
