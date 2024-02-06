#!/usr/bin/python3
""" define write_file """


def write_file(filename="", text=""):
    """Write  the given text into the specified filename."""
    with open(filename, 'w', encoding='utf-8') as file:
        return file.write(text)
