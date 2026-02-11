#!/usr/bin/python3
"""Module that defines a function to generate Pascal's triangle."""


def pascal_triangle(n):
    """Return a list of lists representing Pascal's triangle of n.

    Args:
        n (int): The number of rows of the triangle.

    Returns:
        list: A list of lists of integers representing Pascal's triangle.
        Returns an empty list if n <= 0.
    """
    if n <= 0:
        return []

    triangle = []

    for i in range(n):
        if i == 0:
            triangle.append([1])
        else:
            prev = triangle[-1]
            row = [1]
            for j in range(1, i):
                row.append(prev[j - 1] + prev[j])
            row.append(1)
            triangle.append(row)

    return triangle
