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
