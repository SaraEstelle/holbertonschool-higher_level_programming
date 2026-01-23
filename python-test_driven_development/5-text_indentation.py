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
    if type(text) is not str:
        raise TypeError("text must be a string")

    new_line = False

    for char in text:
        if new_line is False:
            if char == ' ':
                continue
            else:
                new_line = True

        if char in ".?:":
            print(char)
            print()
            new_line = False
        else:
            print(char, end="")
