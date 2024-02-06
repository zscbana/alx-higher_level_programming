#!/usr/bin/python3
"""A script that adds all arguments to a Python
list and saves them to a file."""

import sys
from os.path import exists
from json import dumps
from importlib import import_module


load_module = import_module("6-load_from_json_file")
load_from_json_file = load_module.load_from_json_file


save_to_json_file = import_module("5-save_to_json_file").save_to_json_file

if not exists("add_item.json"):
    with open("add_item.json", "w") as file:
        file.write("[]")

my_list = load_from_json_file("add_item.json")

my_list.extend(sys.argv[1:])

save_to_json_file(my_list, "add_item.json")
