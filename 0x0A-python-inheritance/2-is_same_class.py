#!/usr/bin/python3
""" Module for mylist class. """

def is_same_class(obj, a_class):
    """ Check if an object belongs to the same class as another one.
        Args:
            obj (object) : The object we want to check.
            a_class (type) : The class we compare with.
        Returns:
            bool : True if both objects belong to the same class, False otherwise.
    """
    return type(obj).__name__ == a_class.__name__

