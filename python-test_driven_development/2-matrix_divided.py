#!/usr/bin/python3
"""
This module provides a function that divides all elements of a matrix.
It validates the matrix structure and the divisor before performing
the division and returns a new matrix with rounded results.
"""


def matrix_divided(matrix, div):
    """Divide all elements of a matrix by a number.

    Returns a new matrix with elements rounded to 2 decimals.
    """
    # Validate matrix is a list of lists
    if (not isinstance(matrix, list) or
            any(not isinstance(row, list) for row in matrix)):
        raise TypeError("matrix must be a matrix (list of lists) "
                        "of integers/floats")

    # Validate all elements are int/float
    for row in matrix:
        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) "
                                "of integers/floats")

    # Validate all rows have same size
    row_length = len(matrix[0])
    if any(len(row) != row_length for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    # Validate div
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Return new matrix
    return [[round(element / div, 2) for element in row] for row in matrix]
