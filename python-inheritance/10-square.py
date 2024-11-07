#!/usr/bin/python3
"""
This module defines a Square class that inherits from Rectangle.
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Represents a square, which is a special type of rectangle with equal width and height.
    """

    def __init__(self, size):
        """
        Initializes a new Square instance with validated size.

        :param size: The size of the square sides; must be a positive integer
        :raises TypeError: If size is not an integer
        :raises ValueError: If size is not a positive integer
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """
        Calculates and returns the area of the square.
        
        :return: The area of the square (size * size)
        """
        return self.__size ** 2
