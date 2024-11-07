#!/usr/bin/python3
"""
This module defines a Rectangle class that inherits from BaseGeometry.
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Represents a rectangle, inheriting from BaseGeometry for validation and area calculation.
    """

    def __init__(self, width, height):
        """
        Initializes a new Rectangle instance with validated width and height.

        :param width: The width of the rectangle; must be a positive integer
        :param height: The height of the rectangle; must be a positive integer
        :raises TypeError: If width or height is not an integer
        :raises ValueError: If width or height is not a positive integer
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """
        Calculates and returns the area of the rectangle.
        
        :return: The area of the rectangle (width * height)
        """
        return self.__width * self.__height

    def __str__(self):
        """
        Returns a string representation of the rectangle in the format: [Rectangle] <width>/<height>.
        
        :return: String description of the rectangle
        """
        return f"[Rectangle] {self.__width}/{self.__height}"
