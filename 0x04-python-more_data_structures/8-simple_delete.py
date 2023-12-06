#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    """
    deletes a key in a dictionary.
    Args:
        a_dictionary: input dictionary
        key="": string input key
    Returns:
        The updated dictionary
    """
    if key in a_dictionary:
        del a_dictionary[key]
    return a_dictionary
