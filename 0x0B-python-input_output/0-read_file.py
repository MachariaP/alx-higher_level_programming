#!/usr/bin/python3
"""Module for read_file method"""


def read_file(filename=" "):
    """
    Reads a text file and prints its content to stdout.

    Args:
        filename (str): The name of the text file.
    """

    with open(filename, 'r', encoding='utf-8') as file:
        content = file.read()
        print(content, end="")
