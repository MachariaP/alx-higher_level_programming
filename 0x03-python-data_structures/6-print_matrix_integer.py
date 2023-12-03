#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    """
    Prints a matrix of integers.
    Args:
        matrix=[[]]: input matrix
    Returns:
        Matrix of integers
    """
    if not matrix:
        return None
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print("{:d}".format(matrix[i][j]), end="")
            if (j != len(matrix[i]) - 1):
                print(" ", end="")
        print("")
