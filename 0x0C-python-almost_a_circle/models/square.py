#!/usr/bin/python3
"""Module for Square class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """A square class"""

    def __init__(self, size, x=0, y=0, id=None):
        """Constructor"""

        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
        returns string info about the square
        """

        return '[{}] ({}) {}/{} - {}'.format(
            type(self).__name__,
            self.id,
            self.x,
            self.y,
            self.width
            )

    @property
    def size(self):
        """defines size of square"""
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Update method for square class"""


        if args:
            attributes = ["id", "size", "x", "y"]
            for i, value in enumerate(args):
                setattr(self, attributes[i], value)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Convert Square instance to dictionary"""

        return {
                'id': self.id,
                'x': self.x,
                'size': self.size,
                'y': self.y
                }
