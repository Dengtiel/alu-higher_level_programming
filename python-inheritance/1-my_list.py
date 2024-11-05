#!/usr/bin/python3


class MyList(list):
    """A list subclass with additional functionality to print the list in sorted order."""

    def print_sorted(self):
        """Prints the list elements in ascending order without modifying the original list."""
        print(sorted(self))
