#!/usr/bin/python3
"""A function that appends text to a file."""


def append_write(filename="", text=""):
    """Append text to the end of a file.

    Args:
        filename (str): The name of the file to which
        the text will be appended.
        text (str): The text to append to the file.

    Returns:
        int: The number of characters written to the file.
    """
    with open(filename, 'a', encoding="utf-8") as file:
        return file.write(text)
