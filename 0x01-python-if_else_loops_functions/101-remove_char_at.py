#!/usr/bin/python3
def remove_char_at(str, n):
    copy = ""
    if n < 0:
        return str
    if n >= len(str):
        return str
    for i in range(len(str)):
        if i == n:
            continue
        copy = copy + str[i]
    return copy
