#!/usr/bin/python3
"""matrix division module"""


def matrix_divided(matrix, div):
    """dividing matrix elements by div

    args:
        matrix: list of lists of nums
        div: number to divide upon

    Returns:
        resulted new_matrix after division
    """
    if not isinstance(matrix, list):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    for arr in matrix:
        if not isinstance(arr, list):
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    new_matrix = []
    if len(matrix) == 0:
        return new_matrix

    for arr in matrix:
        for elem in arr:
            if type(elem) not in [int, float]:
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    length = len(matrix[0])
    for arr in matrix:
        if not length == len(arr):
            raise TypeError("Each row of the matrix must have the same size")

    if type(div) not in [int, float]:
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    listy= []
    for arr in matrix:
        for elem in arr:
            listy.append(round(elem / div, 2))
        new_matrix.append(list(listy))
        listy.clear()
    return new_matrix
