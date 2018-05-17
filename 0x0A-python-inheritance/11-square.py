#!/usr/bin/python3
"""

Module has superclass BaseGeometry. Class Rectangle is a subclass


"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Square inherits from Rectangle
    """
    def __init__(self, size):
        """Instances instantiates with size"""
        super().integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)
