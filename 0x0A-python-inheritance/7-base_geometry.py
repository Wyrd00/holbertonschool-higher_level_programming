#!/usr/bin/python3
"""

Module has one class - BaseGeometry


"""


class BaseGeometry:
    """
    class BaseGeometry that requires no attributes
    """
    def area(self):
        """public instance method to calculate area of geomtry"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validatest that the name is str and value is an integer"""
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
        self.__name = name
        self.__value = value
