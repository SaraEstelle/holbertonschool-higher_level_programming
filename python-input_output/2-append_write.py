#!/usr/bin/python3
"""Module that defines a function to append text to a file."""


def append_write(filename="", text=""):
    """Append a string to the end of a UTF-8 text file.

    Args:
        filename (str): The name of the file.
        text (str): The text to append.

    Returns:
        int: The number of characters added.
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
