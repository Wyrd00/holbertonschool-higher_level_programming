#!/usr/bin/python3
"""

Module with function read_file

"""


def read_file(filename=""):
    """read file, must use with statement"""
    with open(filename, encoding="utf-8") as f:
        print(f.read())
