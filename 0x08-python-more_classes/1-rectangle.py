#!/usr/bin/python3
"""
Define a class rectangle
"""


class Rectangle:
    """A class that represents a rectangle."""
    def __init__(self, width=0, height=0):
        """Initialize the rectangle"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Getter from the privte instance attributs witdh"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter for the private attribute width with validation"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Getter from the privte instance attributs height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter for the private attribute height with validation"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__width = value
