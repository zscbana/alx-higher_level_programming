#!/usr/bin/python3
""" Module for BaseGeometry Class. """


class BaseGeometry:
    """ Class representing a base geometry object."""
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if type(value) is not int:
            raise TypeError("<name> must be an integer")
        elif value <= 0:
            raise ValueError("<name> must be greater than 0")
