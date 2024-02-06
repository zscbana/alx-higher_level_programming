#!/usr/bin/python3
""" Module for Square SubClass. """
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ Class representing a square figure. """
    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        '''Area of squre'''
        return self.__size ** 2
