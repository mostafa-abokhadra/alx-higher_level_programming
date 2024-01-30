#!/usr/bin/python3
def assign_value(n, v):
    n = v
    print(n, v)
    print(id(n))
    print(id(v))

l1 = [1, 2, 3]
l2 = [4, 5, 6]
assign_value(l1, l2)
print(id(l1))
print(id(l2))
print(l1)
