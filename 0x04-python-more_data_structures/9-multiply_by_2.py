#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    listy = [a_dictionary[i] * 2 for i in a_dictionary]
    dic = {}
    num = 0
    for i in (a_dictionary):
        dic[i] = listy[num]
        num = num + 1
    return dic
