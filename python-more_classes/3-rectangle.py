#!/usr/bin/python3
"""
This module defines the Rectangle class, representing a rectangle
with width and height properties, and methods for calculating
area and perimeter.
"""


class Rectangle:
    """Represents a rectangle with width and height properties."""

    def __init__(self, width=0, height=0):
        """Initializes a rectangle with optional width and height."""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Getter for the width property."""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter for the width property."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Getter for the height property."""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter for the height property."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calculates the area of the rectangle."""
        return self.width * self.height

    def perimeter(self):
        """Calculates the perimeter of the rectangle."""
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)

    def __str__(self):
        """Returns a string representation of the rectangle using '#' characters."""
        if self.width == 0 or self.height == 0:
            return ""
        return "\n".join("#" * self.width for _ in range(self.height))

    def __repr__(self):
        """Returns a string representation of the rectangle for debugging."""
        return f"<{self.__class__.__module__}.{self.__class__.__name__} object at {hex(id(self))}>"

# Testing the Rectangle class
if __name__ == "__main__":
    my_rectangle = Rectangle(2, 4)
    print("Area: {} - Perimeter: {}".format(my_rectangle.area(), my_rectangle.perimeter()))

    print(str(my_rectangle))     # Print using str()
    print(repr(my_rectangle))    # Print using repr()
    print(my_rectangle)          # Print using print(my_rectangle)

    print("--")  # Separator for clarity
    my_rectangle2 = Rectangle(10, 3)
    print(str(my_rectangle2))    # Print a larger rectangle
    print(repr(my_rectangle2))    # Print using repr()
    print(my_rectangle2)          # Print my_rectangle2
