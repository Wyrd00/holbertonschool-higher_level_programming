#!/usr/bin/python3
"""

Module for checking if class is directly or indirectly inherited

"""


def inherits_from(obj, a_class):
    """returns true if obj is subclass of a_class, else false"""
    return issubclass(obj, a_class)
