#!/usr/bin/python3

def print_square(size):
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
