#!/usr/bin/python3
"""Print a square with the character #."""


def print_square(size):
    """Print a square with the character #.

    Args:
        size (int): size length of the square.

    Raises:
        TypeError: if size is not an integer.
        ValueError: if size < 0.
    """
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")

    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    for _ in range(size):
        print("#" * size)
