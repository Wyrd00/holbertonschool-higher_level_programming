#!/usr/bin/python3
"""

Module with one function: to_json_string

"""
import json


def to_json_string(my_obj):
    """returns json representation of an obj(str)"""
    return json.dumps(my_obj, sort_keys=True)
