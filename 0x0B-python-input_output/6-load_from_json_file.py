#!/usr/bin/python3
"""a function that creates an Object from a “JSON file”:"""
import json


def load_from_json_file(filename):
    """load data from a filename using the json module's loads() method."""
    with open(filename, "r", encoding="utf-8") as file:
        return json.load(file)
