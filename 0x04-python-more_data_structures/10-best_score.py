#!/usr/bin/python3
def best_score(a_dictionary):
    """
    returns a key with the biggest integer value.
    Args:
        a_dictionary: input dictionary
    Returns:
        Key with biggest value
    """
    if a_dictionary is None:
        return None
    maximum_value = 0
    maximum_key = None

    for k, v in a_dictionary.items():
        if v > maximum_value:
            maximum_key = k
            maximum_value = v
    return maximum_key
