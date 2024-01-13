#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    count = 0
    while count < x:
        try:
            if isinstance(my_list[count], int):
                print("{:d}".format(my_list[count]), end="")
            count += 1
        except Exception as err:
            raise err
    if not x == 0:
        print()
    return count
