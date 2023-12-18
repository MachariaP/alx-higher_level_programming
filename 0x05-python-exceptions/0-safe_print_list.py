#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    """
        safe_print_list - prints x elements of a list.
        Args:
            my_list=[]: input list
            x: number of elements to print
        Returns:
            real number of elements printed
    """
    result = 0
    try:
        for i in range(x):
            print(my_list[i], end=' ')
            result += 1
    except IndexError:
        None
    print()
    return result
