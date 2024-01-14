#!/usr/bin/python3
"""Module for Rectangle class"""

from models.base import Base

class Rectangle(Base):
    """Rectangle class inherits from Base.

    Attributes:
        __width (int): Width of the rectangle.
        __height (int): Height of the rectangle.
        __x (int): X-coordinate of the rectangle.
        __y (int): Y-coordinate of the rectangle.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize the Rectangle class.

        Args:
            width (int): Width of the rectangle.
            height (int): Height of the rectangle.
            x (int, optional): X-coordinate of the rectangle (default is 0).
            y (int, optional): Y-coordinate of the rectangle (default is 0).
            id (int, optional): Unique identifier (default is None).
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Getter method for width."""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter method for width."""
        self.validate_integer("width", value, False)
        self.__width = value

    @property
    def height(self):
        """Getter method for height."""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter method for height."""
        self.validate_integer("height", value, False)
        self.__height = value

    @property
    def x(self):
        """Getter method for x."""
        return self.__x

    @x.setter
    def x(self, value):
        """Setter method for x."""
        self.validate_integer("x", value)
        self.__x = value

    @property
    def y(self):
        """Getter method for y."""
        return self.__y

    @y.setter
    def y(self, value):
        """Setter method for y."""
        self.validate_integer("y", value)
        self.__y = value

    def validate_integer(self, name, value, positive=True):
        """Method for validating all setter methods and instantiation"""

        if not isinstance(value, (int, bool)):
            raise TypeError("{} must be an integer".format(name))
        if positive and value < 0:
            raise ValueError("{} must be >= 0".format(name))
        elif not positive and value <= 0:
            raise ValueError("{} must be > 0".format(name))

    def area(self):
        """Returns the area value of the Rectangle instance."""

        return self.__height * self.__width

    def display(self):
        """
        Display the rectangle based on width, height, x and y and character #

        """

        for _ in range(self.__y):
            print()
        for _ in range(self.__height):
            print(" " * self.__x + "#" * self.__width)

    def __str__(self):
        """
        Returns string info about the rectangle
        """

        return '[{}] ({}) {}/{} - {}/{}'.format(
                type(self).__name__,
                self.id,
                self.x,
                self.y,
                self.width,
                self.height)
