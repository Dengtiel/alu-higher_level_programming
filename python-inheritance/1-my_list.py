#!/usr/bin/python3
"""
This module contains a class MyList which is a subclass of the built-in list class.
It includes an additional method to print the list in sorted order without modifying the original list.
"""


class MyList(list):
    """A list subclass with a method to print the list in sorted order."""

    def print_sorted(self):
        """Prints the list in ascending order without modifying the original list."""
        print(sorted(self))
