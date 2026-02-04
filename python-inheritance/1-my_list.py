#!/usr/bin/python3
"""Defines a class MyList that inherits from list."""

class MyList(list):
    """Represents a list with additional functionality."""
    def print_sorted(self):
        """Prints the list in ascending sorted order."""
        print(sorted(self))
