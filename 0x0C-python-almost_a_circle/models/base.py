#!/usr/bin/python3
"""Module first class Base"""


import json

class Base:
    """Base class for managing id attributes"""


    __nb__objects = 0

    def __init__(self, id=None):
        """Initialize Base instance"""

        if id is not None:
            self.id = id
        else:
            Base.__nb__objects += 1
            self.__id = Base.__nb__objects

    @property
    def id(self):
        """Getter method for id."""

        return self.__id

    @id.setter
    def id(self, value):
        """Setter method for id."""

        self__id = value

    @staticmethod
    def to_json_string(list_dictionaries):
        """Convert a list of dictionaries to a JSON string"""
        if list_dictionaries is None or not list_dictionaries:
            return "[]"
        return json.dumps(list_dictionaries)
