#!/usr/bin/python3

def print_list_integer(my_list=[]):
    """
    Print all integers of a list, one integer per line.

    Args:
    - my_list (list): The list containing integers.

    Returns:
    - None
    """
    for num in my_list:
        print("{}".format(num))
