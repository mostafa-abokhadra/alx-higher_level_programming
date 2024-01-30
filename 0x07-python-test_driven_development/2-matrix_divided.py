#!usr/bin/python3
"""matrix division module"""


def matrix_divided(matrix, div):
    """dividing matrix elements by div

        args:
            matrix: list of lists of nums
            div: number to divide upon

        Returns:
            resulted new_matrix after division
    """

    # not a list error 
    if not isinstance(matrix, list):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    # not a list of lists error
    for arr in matrix:
        if not isinstance(arr, list):
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
    
    if __name__ == "__main__":
        import doctest
        doctest.testfile("tests/2-matrix_divided.txt")
