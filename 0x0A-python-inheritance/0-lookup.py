#!/usr/bin/python3
""" Module for lookup method """


def lookup(obj):
    '''Looks up
    Args:
        obj: object to list
    Return:
        list:of attributes
    '''
    return dir(obj)
