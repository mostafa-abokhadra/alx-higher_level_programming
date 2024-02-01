#!/usr/bin/python3
"""multiplying matrix module"""


def check_list(listy):
    if not isinstance(listy, list):
        return True


def check_list_of_lists(listy):
    for arr in listy:
        if not isinstance(arr, list):
            return True


def check_empty(listy):
    if not listy or not listy[0]:
        return True


def check_int_float(listy):
    for arr in listy:
        for elem in arr:
            if type(elem) not in [int, float]:
                return True


def check_notEqual_lists(listy):
    if len(listy) > 1:
        for i in range(1, len(listy)):
            if not len(listy[i]) == len(listy[0]):
                return True


def check_canNot_multiplied(listy_1, listy_2):
    """for two matrices to be multiplied
    the number of columns in the first matrix
    must equal the number of rows in the second matrix
    """
    if not len(listy_1[0]) == len(listy_2):
        return True


def solve(listy1, listy2):
    counter, i, j, sumy = 0, 0, 0, 0
    new_mat, new_list, final_mat = [], [], []

    while counter < len(listy1):
        j = 0
        for k in range(len(listy2)):
            for l in range(len(listy2[k])):
                new_list.append(listy1[i][j] * listy2[k][l])
            j += 1
            new_mat.append(list(new_list))
            new_list.clear()
        for m in range(len(new_mat[0])):
            for q in range(len(new_mat)):
                sumy += new_mat[q][m]
            new_list.append(sumy)
            sumy = 0
        final_mat.append(list(new_list))
        new_mat.clear()
        new_list.clear()
        counter += 1
        i += 1
    return final_mat


def matrix_mul(m_a, m_b):
    """starting point of the program
    
    args:
        m_a: first mat
        m_b: second mat

    Returns:
        final matrix
    """
    if check_list(m_a):
        raise TypeError("m_a must be a list")
    if check_list(m_b):
        raise TypeError("m_b must be a list")
    if check_list_of_lists(m_a):
        raise TypeError("m_a must be a list of lists")
    if check_list_of_lists(m_b):
        raise TypeError("m_b must be a list of lists")
    if check_empty(m_a):
        raise ValueError("m_a can't be empty")
    if check_empty(m_b):
        raise ValueError("m_b can't be empty")
    if check_int_float(m_a):
        raise TypeError("m_a should contain only integers or floats")
    if check_int_float(m_b):
        raise TypeError("m_b should contain only integers or floats")
    if check_notEqual_lists(m_a):
        raise TypeError("each row of m_a must be of the same size")
    if check_notEqual_lists(m_b):
        raise TypeError("each row of m_b must be of the same size")
    if check_canNot_multiplied(m_a, m_b):
        raise ValueError("m_a and m_b can't be multiplied")
    return solve(m_a, m_b)
