#!/usr/bin/python3
"""class to json module"""
import json


def class_to_json(obj):
    """class to json

    args:
        obj: object to convert
    """
    return json.dumps(obj.__dict__)
