#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    """Computes the square value of all integers of a matrix.

    Args:
        matrix (list of lists of integers): The matrix to be squared.

    Returns:
        A new matrix representing the square value of the input matrix.
    """
    return [[element ** 2 for element in row] for row in matrix]
