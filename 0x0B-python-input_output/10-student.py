#!/usr/bin/python3
""" class Student """


class Student:
    """ A representation of a student."""
    def __init__(self, first_name, last_name, age):
        """"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ Returns a dictionary representation of a Student instance. """
        try:
            for attr in attrs:
                if type(attr) is not str:
                    return self.__dict__
        except Exception:
            return self.__dict__
        my_dict = dict()
        for key, value in self.__dict__.items():
            if key in attrs:
                my_dict[key] = value
        return my_dict
