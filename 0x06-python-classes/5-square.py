#!/usr/bin/python3
"""Square Module"""


class Square:
    """Defines square"""

    def __init__(self, size=0):
        """
        Constructor
        Args:
            size: length of one side
        """
        self.size = size

    @property
    def size(self):
        """
        Length of side of square
        Raises:
            ValueError: if size is less than 0
            TypeError: if size is not int
        """
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Area of square
        Returns: Size squared
        """
        return self.__size ** 2

    def my_print(self):
        """Prints square with input size"""
        for i in range(self.size):
            for j in range(self.size):
                print("#", end="\n" if j is self.size - 1 and i != j else "")
        print()
