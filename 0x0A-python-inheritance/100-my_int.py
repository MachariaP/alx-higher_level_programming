#!/usr/bin/python3
"""method for MyInt class"""


class MyInt(int):
    """rebel version of int"""
    def __new__(cls, *args, **kwargs):
        """new instance of class"""
        return super(MyInt, cls).__new__(cls, *args, **kwargs)

    def __eq__(self, param):
        """inverts the != functionality """
        return int(self) != param

    def __ne__(self, param):
        """inverts the == functionality"""
        return int(self) == param
