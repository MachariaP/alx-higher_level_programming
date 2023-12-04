#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    """
    deletes the item at a specific position in a list
    Args:
        my_list=[]: integer list
        idx: index to be deleted
    Returns:
        new list
    """
    if (idx >= 0) and (idx < len(my_list)):
        del my_list[idx]
    return my_list
