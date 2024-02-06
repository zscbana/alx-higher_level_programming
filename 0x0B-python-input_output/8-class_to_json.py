#!/usr/bin/python3
""" a class object to JSON format."""


def class_to_json(obj):
    """Convert a class object to JSON format."""
    return obj.__dict__
