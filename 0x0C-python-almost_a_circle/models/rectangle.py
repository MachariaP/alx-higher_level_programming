#!/usr/bin/python3
""Module class Rectangle"""


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
        self.validate_positive_integer("width", value)
        self.__width = value

    @property
    def height(self):
        """Getter method for height."""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter method for height."""
        self.validate_positive_integer("height", value)
        self.__height = value

    @property
    def x(self):
        """Getter method for x."""
        return self.__x

    @x.setter
    def x(self, value):
        """Setter method for x."""
        self.validate_non_negative_integer("x", value)
        self.__x = value

    @property
    def y(self):
        """Getter method for y."""
        return self.__y

    @y.setter
    def y(self, value):
        """Setter method for y."""
        self.validate_non_negative_integer("y", value)
        self.__y = value

    def validate_positive_integer(self, attribute_name, value):
        """Validate that the value is a positive integer."""
        if not isinstance(value, int):
            raise TypeError(f"{attribute_name} must be an integer")
        elif value <= 0:
            raise ValueError(f"{attribute_name} must be > 0")

    def validate_non_negative_integer(self, attribute_name, value):
        """Validate that the value is a non-negative integer."""
        if not isinstance(value, int):
            raise TypeError(f"{attribute_name} must be an integer")
        elif value < 0:
            raise ValueError(f"{attribute_name} must be >= 0")
