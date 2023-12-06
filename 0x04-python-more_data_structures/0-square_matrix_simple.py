#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_mat = []
    for i in range(len(matrix)):
        a_list = map(lambda arg: arg**2, matrix[i])
        new_mat.append(list(a_list))
    return new_mat
    # another simpler method
    """new_list = []
    new_mat = []
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            new_list.append(matrix[i][j]**2)
        new_mat.append(list(new_list))
        new_list.clear()
    return new_mat
    """
