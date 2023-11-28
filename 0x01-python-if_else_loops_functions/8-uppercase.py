#!/usr/bin/python3
def uppercase(str):
    for i in str:
        if i >= 97 and i <= 110:
            str[i] += 32
