#!/usr/bin/python3
"""
This module provides a function that prints a text with
two new lines after each '.', '?' and ':' character.
"""


def text_indentation(text):
    """Prints text with two new lines after '.', '?' and ':'.

    Args:
        text (str): The input text to format.

    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    separators = ['.', '?', ':']
    buffer = ""

    for char in text:
        buffer += char
        if char in separators:
            print(buffer.strip())
            print()
            buffer = ""

    if buffer.strip():
        print(buffer.strip())
