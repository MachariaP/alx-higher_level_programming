#!/usr/bin/python3
"""Rectangle Module"""


class Rectangle:
    """Defines rectangle"""

    def __init__(self, width: int = 0, height: int = 0):
        """
        constructor

        Args:
            width: width of rectangle
            height: height of rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        Returns the width of a Rectangle object.

        Returns:
            int: The width of the rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Sets and updates the width of a Rectangle object.

        Args:
            value (int): The width value

        Raises:
            TypeError: when the value is not an integer.
            ValueError: when the value provided is less than zero
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Gets or sets height of rectangle
        Returns:
            ValueError: if height is less than 0
            TypeError: if height not integer
        """
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >=0")
        self.__height = value
