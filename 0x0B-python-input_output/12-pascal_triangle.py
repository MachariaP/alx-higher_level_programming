#!/usr/bin/python3
"""Module for pascal_triangle method"""


def pascal_triangle(n):
    """returns a list of lists of integers
    representing the Pascal’s triangle of n"""
    if n <= 0:
        return []
    triangle = []

    for i in range(n):
        row = []
        for j in range(i + 1):
            if j == 0 or j == i:
                row.append(1)
            else:
                prev_row = triangle[i - 1]
                row.append(prev_row[j - 1] + prev_row[j])
        triangle.append(row)
    return (triangle)
