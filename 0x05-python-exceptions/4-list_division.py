#!/usr/bin/python3


def list_division(my_list_1, my_list_2, list_length):

    listy = []
    for i in range(0, list_length):
        try:
            res = my_list_1[i] / my_list_2[i]
            listy.append(res)
        except ZeroDivisionError:
            listy.append(0)
            print("division by 0")
        except TypeError:
            listy.append(0)
            print("wrong type")
        except IndexError:
            listy.append(0)
            print("out of range")
    return listy
