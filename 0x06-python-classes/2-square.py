#!/usr/bin/python3

"""square Module"""


class Square:

    """Defines a square class"""
    def __init__(self, size=0):

        """Initializes a new instance of the Square class."""

        self.__size = size

        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")
