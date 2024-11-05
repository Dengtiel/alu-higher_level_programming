#!/usr/bin/python3
class MyList(list):
    """A list subclass with a method to print the list in sorted order."""


    def print_sorted(self):
        """Prints the list in ascending order without modifying it."""
        print(sorted(self))
