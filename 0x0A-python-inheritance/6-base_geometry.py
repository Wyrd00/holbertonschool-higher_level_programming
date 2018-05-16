#!/usr/bin/python3
"""

Module has one class - BaseGeometry


"""


class BaseGeometry:
    """
    class BaseGeometry that requires no attributes
    """
    #init not necessary, inherits object's init
    def area(self):
        """public instance method to calculate area of geomtry"""
        raise Exception("area() is not implemented")
