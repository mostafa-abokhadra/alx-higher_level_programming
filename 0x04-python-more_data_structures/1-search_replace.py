#!/usr/bin/python3
def search_replace(my_list, search, replace):
    # first method of solving succeded
    """new_list = my_list[:]
    for i in range(len(new_list)):
        if new_list[i] == search:
            new_list[i] = replace
    return new_list
    """
    # second method of sloving succeded
    new_list = [i if i != search else replace for i in my_list]
    return new_list
