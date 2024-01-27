#!usr/bin/python3

def matrix_divided(matrix, div):
    # not a list error 

    if type(matrix) not in [list]:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    # empty list
    new_matrix = []
    if len(matrix) == 0:
        return new_matrix

    # if contains any other types
    for arr in matrix:
        for elem in arr:
            if type(elem) not in [int, float]:
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    # if size of lists not equal
    length = len(matrix[0])
    for arr in matrix:
        if not length == len(arr):
            raise TypeError("Each row of the matrix must have the same size")

    # if wrong div type
    if type(div) not in [int, float]:
        raise TypeError("div must be a number")

    # if div equals to zeor
    if div == 0:
        raise ZeroDivisionError("division by zero")

    listy= []
    for arr in matrix:
        for elem in arr:
            listy.append(round(elem / div, 2))
        new_matrix.append(list(listy))
        listy.clear()
    return new_matrix