#!/usr/bin/python3
def uniq_add(my_list=[]):
    """
    adds all unique integers in a list (only once for each integer).
    Args:
        my_list=[]: input list
    Returns:
        sum of unique ints
    """
    unique_intergers = set()
    total = 0

    for number in my_list:
        if number not in unique_intergers:
            unique_intergers.add(number)
            total += number

    return total
