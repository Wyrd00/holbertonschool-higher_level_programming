#!/usr/bin/python3
"""

Module with one function: class_to_json

"""


def class_to_json(obj):
    """turn obj into serialized"""
    return obj.__dict__
