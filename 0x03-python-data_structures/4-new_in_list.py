#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    """
    Replaces an element in a list at a specific
    position without modifying the original list.
    Args:
        my_list: List input
        idx: index to be replaced
        element: element to replace with.
    Returns:
        Modified list
    """
    if (idx < 0) or (idx >= len(my_list)):
        return my_list
    my_list_copy = my_list.copy()
    my_list_copy[idx] = element
    return my_list_copy
