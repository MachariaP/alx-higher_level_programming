#!/usr/bin/python3

"""
Matrix division module
"""


def matrix_divided(matrix, div):
    """
    divides all elements of a matrix.
    args:
        matrix: input matrix
        div: number to be divided by
    Returns:
        a new matrix
    Raises:
        TypeError:
            If matrix not a list of lists of integers or floats
            If Each row of the matrix not the same size
            If div must not number (integer or float),
        ZeroDivisionError:
            If div is zero
    """

    if not isinstance(matrix, list) or len(matrix) == 0:
        raise TypeError("matrix must be a matrix (list of lists)" +
                        "of integers/floats")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    for row in matrix:
        if not isinstance(row, list) or len(row) == 0:
            raise TypeError("matrix must be a matrix (list of lists)" +
                            "of integers/floats")
        if len(row) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
        for x in row:
            if not isinstance(x, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists)" +
                                "of integers/floats")
    return [[round(x / div, 2) for x in row] for row in matrix]


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/2-matrix_divided.txt")
