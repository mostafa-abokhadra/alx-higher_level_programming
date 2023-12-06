#!/usr/bin/python3
def common_elements(set_1, set_2):
    # first
    """new_list = []
    for i in set_1:
        if i in set_2:
            new_list.append(i)
    return set(new_list)"""
    # second using list comprehension
    """listy = [i for i in set_1 if i in set_2]
    return set(listy)
    """
    # using some complicated stuff
    new_list = list(filter(lambda arg:  arg in set_2, set_1))
    return new_list
