#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    """
    returns a new dictionary with all values multiplied by 2
    Args:
        a_dictionary: input dictionary
    Returns:
        The updated dictionary
    """
    return {k: v * 2 for k, v in a_dictionary.items()}
