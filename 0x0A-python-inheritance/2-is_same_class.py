#!/usr/bin/python3
"""

Module with one class: is_same_class

"""


def is_same_class(obj, a_class):
    """
    is_same_class returns True is exactly an instance of specified class
    """
    return (type(obj) is a_class)
