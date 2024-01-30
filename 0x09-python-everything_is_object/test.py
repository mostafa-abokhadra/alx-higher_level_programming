#!/usr/bin/python3
l1 = [1, 2, 3]
l2 = l1
print(id(l1))
print(id(l2))
l1 = l1 + [4]
print(id(l1))
print(id(l2))
print(l1)
print(l2)
