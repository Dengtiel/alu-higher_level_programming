#!/usr/bin/python3
"""
This module defines a Rectangle class that inherits from BaseGeometry.
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Represents a rectangle using the BaseGeometry class for validation.
    """

    def __init__(self, width, height):
        """
        Initialize a new Rectangle instance, validating width and height.

        :param width: The width of the rectangle; must be a positive integer
        :param height: The height of the rectangle; must be a positive integer
        :raises TypeError: If width or height is not an integer
        :raises ValueError: If width or height is not a positive integer
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
