#!/usr/bin/python3

"""
Module that adds 2 integers.

add_integer, takes two integer arguments and return their sum.
"""


def add_integer(a, b=98):
    """
    adds 2 integers.
    Args:
        a: first int
        b: second int, default 98
    Returns: sum of a and b
    """
    if type(a) not in (int, float):
        raise TypeError("a must be an integer")
    if type(b) not in (int, float):
        raise TypeError("b must be an integer")
    return int(a) + int(b)


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/0-add_integer.txt")
