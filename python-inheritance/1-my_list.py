#!/usr/bin/python3
class MyList(list):
    """A subclass of list that includes a method to print the list in ascending order."""


    def print_sorted(self):
        """Prints the list, sorted in ascending order."""
        print(sorted(self))
