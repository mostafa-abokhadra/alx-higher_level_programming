#!/usr/bin/python3
"""creating an object from json file module"""
import json


def load_from_json_file(filename):
    """creating python object

    args:
        filename: json file name
    """
    with open(filename, mode='r', encoding='utf-8') as fily:
        return json.loads(fily.read())
