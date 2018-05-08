#!/usr/bin/python3
"""

    Module: Base class - Rectangle


"""


class Rectangle:
    """
        Creating class called Rectangle
    """
    def __init__(self, width=0, height=0):
        """Special instance method __init__ that takes width and height"""
        self.width = width
        self.height = height

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
