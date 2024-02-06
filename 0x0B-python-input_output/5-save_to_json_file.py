#!/usr/bin/python3
"""a function that writes an Object to a text file,
using a JSON representation"""
import json


def save_to_json_file(my_obj, filename):
    """ Save a Python object to a JSON file."""
    with open(filename, "w") as file:
        return file.write(json.dumps(my_obj))
