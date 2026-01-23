#!/usr/bin/python3
"""
Module that provides matrix division functionality.

This module contains a function to divide all elements of a matrix.
"""


def matrix_divided(matrix, div):
    """Divides all elements of a matrix by a number.

    Args:
        matrix: List of lists of integers or floats
        div: Number (integer or float) to divide by

    Returns:
        A new matrix with all elements divided by div, rounded to 2 decimals

    Raises:
        TypeError: If matrix is not a list of lists of integers/floats
        TypeError: If rows have different sizes
        TypeError: If div is not a number
        ZeroDivisionError: If div is zero
    """
    error_msg = "matrix must be a matrix (list of lists) of integers/floats"

    # Check if matrix is a list
    if not isinstance(matrix, list) or len(matrix) == 0:
        raise TypeError(error_msg)

    # Check if matrix is a list of lists with valid elements
    for row in matrix:
        if not isinstance(row, list) or len(row) == 0:
            raise TypeError(error_msg)
        for elem in row:
            if not isinstance(elem, (int, float)):
                raise TypeError(error_msg)

    # Check that each row has the same size
    row_size = len(matrix[0])
    for row in matrix:
        if len(row) != row_size:
            raise TypeError("Each row of the matrix must have the same size")

    # Check if div is a number (integer or float)
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    # Prevent division by zero
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Divide each element and round to 2 decimal places
    new_matrix = [[round(elem / div, 2) for elem in row] for row in matrix]

    return new_matrix
