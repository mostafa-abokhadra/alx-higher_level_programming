#!/usr/bin/python3
"""Module for matrix_divided method"""


def matrix_divided(matrix, div):
    """Divides all elements of a matrix.

    Args:
        matrix: The matrix whoses elements are to be divided by div.
        div: The dividing number.

    Raises:
        TypeError: if matrix is not a list of lists of int or float.
        TypeError: if each row of matrix is not of same size.
        TypeError: if div is neither an int nor float
        ZeroDivisionError: if div is zero

    Returns:
        a new matrix with elements rounded to 2 decimal places.
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
