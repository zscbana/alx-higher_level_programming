#!/usr/bin/python3
""" Module for is_kind_of_class method. """


def is_kind_of_class(obj, a_class):
    """ Check if obj belongs to class or one of its subclasses.

        Args:
            obj (object): Object to be checked.
            a_class (type): Class that we want to check against.

        Returns:
            bool: True if obj belongs to class or
                  one of its subclasses, False otherwise.
    """
    return isinstance(obj, type) and issubclass(obj, a_class) \
        or not isinstance(obj, type) and isinstance(obj, a_class)
