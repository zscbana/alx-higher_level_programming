#!/usr/bin/python3
"""a Python script that takes in a URL, sends a request
to the URL and displays the value of the X-Request-Id"""
import urllib.request
from sys import argv

if len(argv) > 1:
    with urllib.request.urlopen(argv[1]) as response:
        print(response.getheader("X-Request-Id"))
