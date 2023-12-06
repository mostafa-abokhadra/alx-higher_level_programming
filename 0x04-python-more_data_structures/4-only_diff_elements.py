#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    # first
    """new_list = []
    new_list = [i for i in set_1 if i not in set_2]
    new_list += [i for i in set_2 if i not in set_1]
    return set(new_list)
    """
    new_set = set1.difference(set_2)
    return new_set
