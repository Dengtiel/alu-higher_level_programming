#!/usr/bin/python3

"""
Module that defines a Rectangle class with 
attributes, methods, and 
validation to model a rectangular shape.


The Rectangle class supports instance creation with 
optional width and height, 
calculations for area and perimeter, and comparison
of two rectangles based on
their area. It also includes string representation
and class-level tracking 
for the number of instances created.
"""

class Rectangle:
    """
    Rectangle class to represent a rectangle shape.
    
    This class defines the properties of a rectangle including width, height, 
    and provides methods to calculate its area and perimeter. The class also 
    tracks the number of instances and includes string representation methods 
    for printing and debugging.

    Class Attributes:
        number_of_instances (int): 
        A count of the number of Rectangle instances.
        print_symbol (str): 
        The symbol used for string representation of the rectangle.
    """
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """
        Initializes the Rectangle instance
        with optional width and height.
        The class-level counter for instances
        is incremented upon creation.
        
        :param width: The width of the rectangle, default is 0.
        :param height: The height of the rectangle, default is 0.
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """
        Returns the width of the rectangle.
        
        :return: The current width of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Sets the width of the rectangle with 
        validation checks for the type 
        and non-negative value.

        :param value: The width value to set.
        :raises TypeError: If the value is not an integer.
        :raises ValueError: If the value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Returns the height of the rectangle.
        
        :return: The current height of the rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Sets the height of the rectangle with
        validation checks for the type 
        and non-negative value.

        :param value: The height value to set.
        :raises TypeError: If the value is not an integer.
        :raises ValueError: If the value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Calculates and returns the area of the rectangle.

        :return: The area (width * height) of the rectangle.
        """
        return self.width * self.height

    def perimeter(self):
        """
        Calculates and returns the perimeter of the rectangle.
        
        If either width or height is zero, p considered 0.
        
        :return: The perimeter, or 0 if either width or height is 0.
        """
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)

    def __str__(self):
        """
        Returns a string of the rectangle using the print symbol.

        :return: A string consisting of print_symbol to depict rectangle.
        """
        if self.width == 0 or self.height == 0:
            return ""
        return "\n".join([str(self.print_symbol) 
            * self.width for _ in range(self.height)])

    def __repr__(self):
        """
        Returns a formal string for recreating the rectangle.

        :return: A string  used with eval() to create a new instance.
        """
        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        """
        Handles deletion. Decreases the number_of_instances 
        counter and prints a message when the instance is deleted.
        """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        Compares two rectangles and returns the one with the largest area.

        :param rect_1: The first rectangle to compare.
        :param rect_2: The second rectangle to compare.
        :return:  with the largest area, or rect_1 if areas are equal.
        :raises TypeError: If either rect_1 or rect_2 is not an instance.
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2
