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
        self.integer_validator("size", size)
        super().__init__(size, size)

    def __str__(self):
        """creating string for class Square"""
        return "[Square] {}/{}".format(self._Rectangle__width, self._Rectangle__height)
