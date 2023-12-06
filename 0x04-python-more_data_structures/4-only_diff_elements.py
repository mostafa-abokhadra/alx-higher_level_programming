#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    # first
    new_list = []
    new_list = [i for i in set_1 if i not in set_2]
    new_list += [i for i in set_2 if i not in set_1]
    return set(new_list)
    # c style
    """new_list = []
    new_list = func(set_1, set_2)
    new_list += func(set_2, set_1)
    return set(new_list)
def func(set_1, set_2):
    new_list = []
    for i in set_1:
        check = True
        for j in set_2:
            if i != j:
                continue
            check = False
        if check:
            new_list.append(i)
    return new_list
    """
