#!/usr/bin/python3
"""convert from json module"""
import json


def from_json_string(my_str):
    """from json

    args:
        my_str: json format
    """
    return json.loads(my_str)
