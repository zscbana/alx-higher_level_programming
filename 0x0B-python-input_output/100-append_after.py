#!/usr/bin/python3
""" Creating a pascal triangle """


def append_after(filename="", search_string="", new_string=""):
    """append new string affter line which searched for """
    with open(filename, "r") as file:
        line_list = []
        while True:
            line = file.readline()
            if line == "":
                break
            line_list.append(line)
            if search_string in line:
                line_list.append(new_string)
    with open(filename, "w") as f:
        f.writelines(line_list)
