#!/usr/bin/python3
"""Module for write_file method"""


def write_file(filename="", text=""):
    """
    write a string to a text file (UTF8)

    Returns:
        the number of characters written.
    """

    with open(filename, 'w', encoding='utf-8') as file:
        content = file.write(text)
        return content
