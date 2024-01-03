#!/usr/bin/python3

"""
Module that adds 2 integers.

add_integer, that takes two integer arguments and returns their sum.
"""


def add_integer(a, b=98):
    """
    Compute and return the sum of two integers.

    Args:
        a: first integer
        b: second integer, 98 by default

    Returns:
        sum of integer a and integer b

    Tests:
        >>> add_integer(0)
        98
        >>> add_integer(1, -2)
        -1
        >>> add_integer('3', '23')
        Traceback (most recent call last):
        ...
        TypeError: a must be an integer
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")

    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    try:
        int(a)
        int(b)
    except ValueError as err:
        raise err

    return int(a) + int(b)


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/0-add_integer.txt")
