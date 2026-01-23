#!/usr/bin/python3
"""
Function that prints a square with the character #
"""


def print_square(size):
    """
    Prints a square with the character #

    Args:
        size (int): size of the square

    Raises:
        TypeError: if size is not an integer
        ValueError: if size < 0
    """

    # Validate type
    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    # Validate value
    if size < 0:
        raise ValueError("size must be >= 0")

    # Print the square
    for _ in range(size):
        print("#" * size)
