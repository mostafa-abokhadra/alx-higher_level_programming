#!/usr/bin/python3
def multiply_list_map(my_list=[], number=0):
    listy = list(map(lambda multi: multi * number, my_list))
    return listy
