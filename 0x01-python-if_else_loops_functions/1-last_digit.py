#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last = 0

def get_last(number):
    last = 0
    if number < 0:
        number = number - number - number
        last = number % 10
        last = -last
    else:
        last = number % 10
    return last

last = get_last(number)
if last > 5:
    print(f"Last digit of {number} is {last} and is greater than 5")
elif last == 0:
    print(f"Last digit of {number} is {last} and is 0")
elif last < 6 and last != 0:
    print(f"Last digit of {number} is {last} and is less than 6 and not 0")
