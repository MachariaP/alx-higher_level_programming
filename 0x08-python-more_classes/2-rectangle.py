#!/usr/bin/python3

class Rectangle:
    """
    Rectangle Class

    Defines a rectangle by its width and height attributes.
    """

    def __init__(self, width: int = 0, height: int = 0):
        """
        Initializes a new Rectangle instance.

        Args:
            width (int): width of the rectangle (default is 0).
            height (int): Height of the rectangle (default is 0).
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        Get the width of the rectangle.

        Returns:
            int : width of the rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Sets and updates the width of the rectangle.

        Args:
            value(int): The width value.

        Raises:
            TypeError: when the value is not an integer.
            ValueError: when the value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be greater than or equal to 0")
        self.__width = value

    @property
    def height(self):
        """
        Gets the height of the rectangle.

        Returns:
            int: height of the rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Sets and updates the height of the rectangle

        Args:
            value (int): The height value.

        Raises:
            TypeError: when the value is not an integer.
            ValueError: when the value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be greater than or equal to 0")
        self.__height = value

    def area(self):
        """
        Calculates and returns the area of the rectangle.

        Returns:
            int: The area of the rectangle.
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Calculates and returns the perimeter of the rectangle.

        Returns:
            int: The perimeter of the rectangle.
        """
        return 2 * (self.__width + self.__height) if self.__width and self.__height else 0
