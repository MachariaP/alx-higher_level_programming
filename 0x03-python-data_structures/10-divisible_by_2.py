#!/usr/bin/python3

def divisible_by_2(my_list=[]):

    """
    Find multiples of 2 in a list.

    Args:
        my_list: Integer list

    Returns:
        List of booleans indicating whether each element is a multiple of 2.
    """

    return [num % 2 == 0 for num in my_list] if my_list else None
