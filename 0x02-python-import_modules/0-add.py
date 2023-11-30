#!/usr/bin/python3

"""
This script demonstrates the use of the add function from the add_0 module.

It imports the add function, assigns values to variables a and b, and prints the results of the addation using the add function.
"""

if __name__ == "__main__":

    from add_0 import add

    a = 1
    b = 2

    print("{} + {} = {}".format(a, b, add(a, b)))
