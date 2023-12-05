#!/usr/bin/python3
'''def add_tuple(tuple_a=(), tuple_b=()):
    a = 0
    b = 0
    ll = []
    if len(tuple_a) < 2:
        for i in tuple_a:
            ll.append(i)
        for i in range(len(ll), 2):
            ll.append(0)
        tuple_a = tuple(ll)

    if len(tuple_b) < 2:
        for i in tuple_b:
            ll.append(i)
        for i in range(len(ll), 2):
            ll.append(0)
        tuple_b = tuple(ll)

    a = tuple_a[0] + tuple_b[0]
    b = tuple_a[1] + tuple_b[1]
    newtup = (a, b)
    return newtup'''
def add_tuple(tuple_a=(), tuple_b=()):
    tuple_a += (0, 0)
    tuple_b += (0, 0)
    return(tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
