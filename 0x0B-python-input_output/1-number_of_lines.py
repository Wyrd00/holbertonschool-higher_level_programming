#!/usr/bin/python3
"""

Module with one function: number_of_lines

"""


def number_of_lines(filename=""):
    """return number of lines in filename"""
    with open(filename, encoding="utf-8") as f:
        counter = 0
        for lines in f:
            counter += 1
    return counter
