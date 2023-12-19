#!/usr/bin/python3
"""Square Module"""


class Square:
    """Defines square"""

    def __init__(self, size=0):
        """
        Constructor
        Args:
            size: length of one side
        Raises:
            ValueError: if size is less than 0
            TypeError: if size is not int
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """
        Area of square
        Returns: Size squared
        """
        return self.__size ** 2
