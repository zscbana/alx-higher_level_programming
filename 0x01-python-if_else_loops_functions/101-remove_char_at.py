#!/usr/bin/python3
def remove_char_at(str, n):
    nstr = ""
    for x, c in enumerate(str):
        if x != n:
            nstr += c
    return nstr
