#!/usr/bin/python3
"""Module class Rectangle"""


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
        # Call the constructor of the Base class with the provided id.
        super().__init__(id)

        # Assign the provided values to the corresponding attributes.
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
        # Setter allows validation or additional logic before assigning the value.
        self.__width = value

    @property
    def height(self):
        """Getter method for height."""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter method for height."""
        # Setter allows validation or additional logic before assigning the value.
        self.__height = value

    @property
    def x(self):
        """Getter method for x."""
        return self.__x

    @x.setter
    def x(self, value):
        """Setter method for x."""
        # Setter allows validation or additional logic before assigning the value.
        self.__x = value

    @property
    def y(self):
        """Getter method for y."""
        return self.__y

    @y.setter
    def y(self, value):
        """Setter method for y."""
        # Setter allows validation or additional logic before assigning the value.
        self.__y = value

