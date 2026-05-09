#!/usr/bin/env python3
"""Module for CountedIterator class"""


class CountedIterator:
    """An iterator that counts the number of items iterated"""

    def __init__(self, iterable):
        """Initializes CountedIterator with an iterable

        Args:
            iterable: any iterable object
        """
        self.iterator = iter(iterable)
        self.count = 0

    def get_count(self):
        """Returns the number of items iterated so far"""
        return self.count

    def __next__(self):
        """Returns the next item and increments the counter"""
        item = next(self.iterator)
        self.count += 1
        return item
