#!/usr/bin/python3
"""writing a json file"""
import json


def save_to_json_file(my_obj, filename):
    """writing json format

    args:
        my_obj: object to be written
        filename: name of file
    """
    with open(filename, mode='w', encoding='utf-8') as fily:
        filename.write(json.dumps(my_obj))
