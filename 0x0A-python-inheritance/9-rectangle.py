#!/usr/bin/python3
"""

Module has superclass BaseGeometry. Class Rectangle is a subclass

"""


class BaseGeometry:
    """
    class BaseGeometry that requires no attributes
    """
    def area(self):
        """when called it will raise an exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validatest that the name is str and value is an integer"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
        self.__name = name
        self.__value = value


class Rectangle(BaseGeometry):
    """
    class Rectangle inherits from BaseGeometry
    """
    def __init__(self, width, height):
        """spec method __init__ take attribute from base, while adding own"""
        super().integer_validator("height", height)
        self.integer_validator("width", width)
        self.__width = width
        self.__height = height

    def area(self):
        """implement area"""
        return self.__width * self.__height

    def __str__(self):
        """creating string for class Rectangle"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
