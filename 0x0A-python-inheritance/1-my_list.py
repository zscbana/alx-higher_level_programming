#!/usr/bin/python3
""" Module for mylist class. """


class MyList(list):
    """ coustem my list class."""
    def print_sorted(self):
        "Method print the sorted list"
        print(sorted(self))
