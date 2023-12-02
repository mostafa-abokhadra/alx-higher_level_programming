#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if idx < 0 or idx >= len(my_list):
        return list(my_list)
    else:
        list2 = list(my_list)
        list2[idx] = element
        return list2
