#!/usr/bin/python3
import sys
if (__name__ == "__main__"):
    from calculator_1 import add, sub, div, mul

    argv = sys.argv
    argc = len(argv) - 1

    if argc != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    a = int(argv[argc - 2])
    b = int(argv[argc])
    operator = argv[argc - 1]
    result = 0

    if operator == '+':
        result = add(a, b)
        print("{} + {} = {}".format(a, b, result))
    elif operator == '-':
        result = sub(a, b)
        print("{} - {} = {}".format(a, b, result))
    elif operator == '/':
        result = div(a, b)
        print("{} / {} = {}".format(a, b, result))
    elif operator == '*':
        result = mul(a, b)
        print("{} * {} = {}".format(a, b, result))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
