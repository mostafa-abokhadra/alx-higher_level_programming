#!/usr/bin/python3
"""convert to json module"""
import json


def to_json_string(my_obj):
    """to json

    args:
        my_obj: object to be converted
    """
    return json.dumps(my_obj)
