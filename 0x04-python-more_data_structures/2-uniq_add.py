#!/usr/bin/python3
def uniq_add(my_list=[]):
    result = 0
    l_set = set(my_list)
    for i in l_set:
        result += i
    return result
