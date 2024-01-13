#!/usr/bin/python3


def list_division(my_list_1, my_list_2, list_length):
    div_list = []
    for i in range(0, list_length):
        try:
            res = my_list_1[i] / my_list_2[i]
        except ZeroDivisionError:
            print("division by 0")
            res = 0
        except (TypeError, ValueError):
            print("wrong type")
            res = 0
        except IndexError:
            print("out of range")
        finally:
            div_list.append(res)
    return div_list
