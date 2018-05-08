#!/usr/bin/python3
"""

    Module: Base class - Rectangle


"""


class Rectangle:
    """
        Creating class called Rectangle with two attribues: width and height
    """
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """Special instance method __init__ that takes width and height"""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    def area(self):
        """Public instance method area that returns area of rectangle"""
        return self.width * self.height

    def perimeter(self):
        """
        Public instance method perimeter that returns perimeter of rectangle
        """
        if self.width == 0 or self.height == 0:
            return 0
        return (self.width * 2) + (self.height * 2)

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Return biggest rectangle base"""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

    def __str__(self):
        """Redefine magic method __str__"""
        if self.width == 0 or self.height == 0:
            return ""
        rect = self.width * str(self.print_symbol)
        for h in range(self.height - 1):
            rect += '\n' + (self.width * str(self.print_symbol))
        return rect

    def __repr__(self):
        """Redefine magic method __repr__"""
        return "Rectangle(" + str(self.width) + ", " + str(self.height) + ")"

    def __del__(self):
        """
        Adding a print to magic method __del__, which print after del <inst>
        """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @property
    def width(self):
        """Getter for width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter for width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Getter for height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter for height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
