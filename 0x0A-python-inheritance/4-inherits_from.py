#!/usr/bin/python3
""" Module for iinherits_from method. """


def inherits_from(obj, a_class):
    """ Check if an object is derived from another class.

        Args:
            obj (object): The instance to check against the base class.
            a_class (type): The base class to compare with.

        Returns:
            bool: True if `obj` is derived from `a_class`, False otherwise.
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
