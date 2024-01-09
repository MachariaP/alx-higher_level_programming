#!/usr/bin/python3
"""Module that defines fctn that adds a new attribute"""


def add_attribute(obj, attribute, value):
    """
        adds a new attribute to an object if it’s possible
        Args:
            obj: input object to add attribute to
            attribute: name of attribute to add to abject
            value: Value of attribute
        Raises:
            TypeError if cannot add attribute
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, attribute, value)
