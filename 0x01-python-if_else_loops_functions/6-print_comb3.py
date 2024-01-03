#!/usr/bin/python3
for x in range(10):
    for i in range(x + 1, 10):
        print("{:d}{:d}".format(x, i), end=", " if x != 8 or i != 9 else "\n")
