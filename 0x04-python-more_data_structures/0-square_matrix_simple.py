#!/bin/usr/python3
def square_matrix_simple(matrix=[]):
    new_list = []
    new_mat = []
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            new_list.append(matrix[i][j]**2)
        new_mat.append(list(new_list))
        new_list.clear()
    return new_mat
