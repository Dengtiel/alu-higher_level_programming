#!/usr/bin/python3
"""
This module defines a class MyList that inherits from the built-in list class.


MyList adds a method to print the list elements in ascending order without modifying
the original list order.
"""

class MyList(list):
    """
    A subclass of the built-in list class with an additional method to
    print the list in ascending order.
    """

    def print_sorted(self):
        """
        Prints the elements of the list in ascending order.

        This method uses Python's built-in sorted function to display
        a sorted version of the list without altering the original order of
        the list elements.
        """
        print(sorted(self))
