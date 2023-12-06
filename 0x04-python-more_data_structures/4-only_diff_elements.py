#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    """
    returns a set of all elements present in only one set.
    Args:
        set_1: first set
        set_2: second set
    Returns:
        set of all elems in one set
    """
    new_set = set_1 ^ set_2

    return new_set
