#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    """
    Prints a list of ints in reverse.
    Args:
        my_list[]: A list ints.
    Returns:
        Reversed list
    """
    if not my_list:
        return None
    for i in reversed(my_list):
        print("{:d}".format(i))
