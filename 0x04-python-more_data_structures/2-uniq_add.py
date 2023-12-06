#!/usr/bin/python3
def uniq_add(my_list=[]):
    result = 0
    l_set = set(my_list)
    for i in l_set:
        result += i
    return result
    # c style
    """if len(my_list) == 0:
        return 0
    res = my_list[0]
    for i in range(1, len(my_list)):
        check = True
        for j in range(i):
            if my_list[i] != my_list[j]:
                continue
            check = False
            break
        if check:
            res += my_list[i]
    return res
    """
