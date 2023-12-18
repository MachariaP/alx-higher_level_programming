#!/usr/bin/python3

def safe_print_list(my_list=[], x = 0):
    """
        safe_print_list - prints x elements of a list
        Args:
            my_list = []: input list
            x: number of elements to print
        Returns:
            real number of elements printed
    """
    try:
        count = 0
        for i in range(x):
            print("{}".format(my_list[i]), end = "")
            count += 1
        print()
        return count
    except IndexError:
        print()
        return count
