#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    """
    replaces or adds key/value in a dictionary
    Args:
        a_dictionary: input dictionary
        key: key
        value: value pair
    Returns:
        The updated dictionary
    """
    a_dictionary[key] = value
    return a_dictionary
