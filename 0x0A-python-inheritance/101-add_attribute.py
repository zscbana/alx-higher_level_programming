#!/usr/bin/python3
"""a function that adds attributes to objects."""


def add_attribute(obj, att, value):
    """Add an attribute and a value to the given object.

    Args:
        obj (object): The object to which we want to add an attribute.
        att (str): The name of the new attribute.
        value: The value associated with the new attribute.

    Returns:
        None
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
