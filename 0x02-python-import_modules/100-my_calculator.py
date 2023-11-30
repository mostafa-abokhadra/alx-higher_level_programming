#!/usr/bin/python3

import sys
import calculator_1 as calc

operators = {"+", "-", "*", "/"}
state = False

if len(sys.argv) < 4:
    print("Usage: ./100-my_calculator.py <a> <operator> <b>")
    sys.exit(1)
# for i in range(len(operators)):
if sys.argv[2] == '+' or sys.argv[2] == '-' or sys.argv[2] == '/' or sys.argv[2] == '*':
    print(sys.argv[2])
    state = True
    #break
if state:
    a = int(sys.argv[1])
    b = int(sys.argv[3])
    if sys.argv[2] == '+':
        print("{} + {} = {}" .format(a, b, calc.add(a, b)))
    elif sys.argv[2] == '-':
        print("{} - {} = {}" .format(a, b, calc.sub(a, b)))
    elif sys.argv[2] == '*':
        print("{} * {} = {}" .format(a, b, calc.mul(a, b)))
    else:
        print("{} / {} = {}" .format(a, b, calc.div(a, b)))
else:
    print(sys.argv[2])
    print("Unknown operator. Available operators: +, -, * and /")
    sys.exit(1)
