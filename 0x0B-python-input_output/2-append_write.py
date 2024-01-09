#!/usr/bin/python3
"""Module for append_write method"""


def append_write(filename="", text=""):
    """
    Appends a string at the end of a text file (UTF8)

    Returns:
        the number of characters added.
    """

    with open(filename, 'a', encoding='utf-8') as file:
        content = file.write(text)
        return content
