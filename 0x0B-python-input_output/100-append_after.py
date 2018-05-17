#!/usr/bin/python3
"""

Module with one function: append_after

"""


def append_after(filename="", search_string="", new_string=""):
    """append text a line after each specific string"""
    with open(filename, 'r', encoding="utf-8") as f:
        new_lists = []
    with open(filename, 'w', encoding="utf-8") as f:
            if line = search_string:
                line.append(line)
