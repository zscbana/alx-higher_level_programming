#!/usr/bin/python3
"""Define class Square"""


class Square:
    """ a square"""

    def __init__(self, size=0):
        """Initialize Square.

        Args:
            size : The size of the new square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
