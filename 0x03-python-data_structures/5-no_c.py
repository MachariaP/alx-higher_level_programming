#!/usr/bin/python3
def no_c(my_string):
    """
    Removes letter c from a string
    Args:
        my_string: input string
    Returns:
        Modified string
    """
    result = ""
    for i in range(len(my_string)):
        if (my_string[i] != 'c') and (my_string[i] != 'C'):
            result += my_string[i]
    return result
