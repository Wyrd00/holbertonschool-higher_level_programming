#!/usr/bin/python3
"""

Module with one function: append_write

"""


def append_write(filename="", text=""):
    """Append to a file and return number of char written"""
    with open(filename, 'a', encoding="utf-8") as f:
        return f.write(text)
