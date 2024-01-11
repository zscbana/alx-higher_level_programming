#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    for x in sorted(a_dictionary.keys()):
        print("{}: {}".format(x, a_dictionary[x] * 2))
