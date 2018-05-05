#!/usr/bin/python3

"""

    Module with one method: print_square(size)

"""


def print_square(size):
    """
        Print a square with parameter size.
        If not int or size < 0, raise Error
    """
    if not isinstance(size, (float, int)):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        print("{}".format("#" * size))
