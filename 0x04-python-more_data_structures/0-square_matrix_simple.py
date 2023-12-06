#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    # create a new matrix with the same size as the input matrix
    result_matrix = []

    # Iterate through each row in the matrix.
    # create a new row for the result matrix
    for row in matrix:
        result_row = []

        # Iterate through each element in the row and square the value
        for element in row:
            squared_value = element ** 2
            result_row.append(squared_value)

        # Add the squared row to the result matrix
        result_matrix.append(result_row)

    return result_matrix
