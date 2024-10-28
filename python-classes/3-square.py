#!/usr/bin/python3
"""Module that defines a square."""


class Square:
    """A class that defines a square by its size."""

    def __init__(self, size=0):
        """Instantiation with optional size."""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size  # Private instance attribute

    def area(self):
        """Public instance method that returns the area of the square."""
        return self.__size ** 2  # Area = size squared

