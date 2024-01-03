#!/usr/bin/python3
for x in range(10):
    for i in range(10):
        print("{:d}{:d}".format(x, i), end="\n" if x == 9 and i == 9 else ", ")
