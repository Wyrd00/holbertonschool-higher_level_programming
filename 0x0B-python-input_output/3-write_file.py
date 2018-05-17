#!/usr/bin/python3
"""

Module with one function: write_file

"""


def write_file(filename="", text=""):
    """Write file return number of char written"""
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
