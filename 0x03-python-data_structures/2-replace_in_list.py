#!/usr/bin/python3

def replace_in_list(my_list, idx, element):
    """
    Replaces an element at a specific position in a list.

    Args:
        my_list (list): A list of integers.
        idx (int): The index to replace the element.
        element: The new element to insert.

    Returns:
        list: The modified list.
    """
    if idx < 0 or idx >= len(my_list):
        return my_list

    my_list[idx] = element

    return my_list
