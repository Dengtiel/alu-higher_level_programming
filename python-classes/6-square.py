#!/usr/bin/python3
"""Module that defines a square."""


class Square:
    """A class that defines a square by its size and position."""

    def __init__(self, size=0, position=(0, 0)):
        """Instantiation with optional size and position."""
        self.size = size  # Use the setter to validate the initial size
        self.position = position  # Use the setter to validate the position

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

    @property
    def position(self):
        """Getter for the position property."""
        return self.__position

    @position.setter
    def position(self, value):
        """Setter for the position property."""
        if (not isinstance(value, tuple) or len(value) != 2 or
                not all(isinstance(i, int) for i in value) or
                any(i < 0 for i in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value  # Private instance attribute

    def area(self):
        """Public instance method that returns the area of the square."""
        return self.__size ** 2  # Area = size squared

    def my_print(self):
        """Public instance method that prints the square with '#'."""
        if self.__size == 0:
            print("")  # Print an empty line if size is 0
            return

        # Print new lines for the vertical position
        for _ in range(self.__position[1]):
            print("")  # Create vertical space

        # Print the square
        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
