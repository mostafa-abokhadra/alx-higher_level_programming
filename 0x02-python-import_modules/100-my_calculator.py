#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    import calculator_1 as calc

    state = False

    if len(sys.argv) < 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    if sys.argv[2] == "+" or sys.argv[2] == "-":
        state = True
    if sys.argv[2] == "*" or sys.argv[2] == "/":
        state = True
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
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
