#!/usr/bin/python3
def common_elements(set_1, set_2):
    """
    returns a set of common elements in two sets.
    Args:
        set_1: first set
        set_2: second set
    Returns:
        set of common elements
    """
    new_set = set_1 & set_2

    return new_set
