#!/usr/bin/python3


def list_division(my_list_1, my_list_2, list_length):
    div_list = []
    for i in range(0, list_length):
        try:
            res = my_list_1[i] / my_list_2[i]
            div_list.append(res)
        except ZeroDivisionError:
            print("division by 0")
            div_list.append(0)
        except TypeError:
            print("wrong type")
            div_list.append(0)
        except IndexError:
            div_list.append(0)
            print("out of range")
        finally:
            pass
    return div_list
