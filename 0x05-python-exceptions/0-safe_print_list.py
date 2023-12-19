#!/usr/bin/python3


def safe_print_list(my_list=[], x=0):
    num = 0
    it = 0
    while it < x:
        try:
            print("{}".format(my_list[it]), end="")
            num += 1
        except:
            break;
        it += 1
    print()
    return num
