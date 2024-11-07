#!/usr/bin/python3
class Rectangle:
    # Class attribute for tracking the number of instances
    number_of_instances = 0
    # Class attribute for setting the print symbol
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """
        Initializes the Rectangle instance with width and height.
        Increment the class attribute number_of_instances upon instantiation.
        

        :param width: Width of the rectangle, default is 0
        :param height: Height of the rectangle, default is 0
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """
        Returns the width of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Sets the width of the rectangle with validation.
        
        :param value: The width to set
        :raises TypeError: If value is not an integer
        :raises ValueError: If value is less than 0
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
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Sets the height of the rectangle with validation.
        
        :param value: The height to set
        :raises TypeError: If value is not an integer
        :raises ValueError: If value is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Calculates the area of the rectangle.
        
        :returns: The area of the rectangle
        """
        return self.width * self.height

    def perimeter(self):
        """
        Calculates the perimeter of the rectangle.
        
        :returns: The perimeter of the rectangle, or 0 if either width or height is 0
        """
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)

    def __str__(self):
        """
        Returns a string representation of the rectangle using the print symbol.
        
        :returns: A string that represents the rectangle using the print symbol
        """
        if self.width == 0 or self.height == 0:
            return ""
        return "\n".join([str(self.print_symbol) * self.width for _ in range(self.height)])

    def __repr__(self):
        """
        Returns a formal string representation for recreating the rectangle.
        
        :returns: A string that can be used with eval() to create a new instance of the rectangle
        """
        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        """
        Handles deletion of a Rectangle instance. Decreases the class attribute number_of_instances 
        and prints a message when the instance is deleted.
        """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        Compares two rectangles and returns the one with the largest area.
        
        :param rect_1: The first rectangle to compare
        :param rect_2: The second rectangle to compare
        :returns: The rectangle with the largest area, or rect_1 if they have the same area
        :raises TypeError: If either rect_1 or rect_2 is not an instance of Rectangle
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2
