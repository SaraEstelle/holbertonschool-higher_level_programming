#!/usr/bin/env python3
"""Counted Iterator : keeping track of iteration."""

class CountedIterator:
    """Iterator that count how many items have been iterated."""

    def __init__(self, iterable):
        self.iterator = iter(iterable)
        self.count = 0

    def __next__(self):
        item = next(self.iterator) # May raise StopIteration
        self.count += 1
        return item

    def get_count(self):
        """Return the number of items that have been iterated so far."""
        return self.count
