#!/usr/bin/python3
""" function that reads a text file (UTF8) and prints it to stdout: """


def read_file(filename=""):
    '''Read file wit encoding utf-8'''
    with open(filename, encoding='utf-8') as file:
        print(file.read(), end='')
