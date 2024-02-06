#!/usr/bin/python3
"""task 8."""


def class_to_json(obj):
    """Converts a class object to json format."""
    return obj.__dict__
