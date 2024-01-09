#!/usr/bin/python3
"""Module for is_same_class method"""


def is_same_class(obj, a_class):
    """checks for an instance of the specified class """
    return type(obj) == a_class
