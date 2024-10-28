#!/usr/bin/python3
"""Module that defines a square."""


class Square:
    """A class that defines a square by its size."""

    def __init__(self, size=0):
        """Instantiation with optional size."""
        self.size = size  # Use the setter to validate the initial size

    @property
    def size(self):
        """Getter for the size property."""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter for the size property."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value  # Private instance attribute

    def area(self):
        """Public instance method that returns the area of the square."""
        return self.__size ** 2  # Area = size squared
