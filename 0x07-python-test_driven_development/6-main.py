#!/usr/bin/python3
max_integer = __import__('6-max_integer').max_integer

print(max_integer([1, 2, 3, 4]))
print(max_integer([1, 3, 4, 2]))
print(max_integer(['a', 'b', 'c']))
print(max_integer(["messi", "maradona", "ronaldinho"]))
print(max_integer([2.5, 66.7, 1.4]))
print(max_integer([["messi"], ["messii"]]))
print(max_integer([("messi", 10), ("messi", 19)]))
print(max_integer({"messi": 30, "messi": 19, "messi": 10}))
