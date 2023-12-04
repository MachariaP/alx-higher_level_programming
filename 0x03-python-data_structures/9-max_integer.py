#!/usr/bin/python3

def max_integer(my_list=[]):

    """
    finds the biggest integer of a list.
    Args:
        my_list: integer list
    Returns:
        biggest integer
    """

    if len(my_list) < 1:
        return None
    list_copy = my_list.copy()
    list_copy.sort()
    return list_copy[-1]
