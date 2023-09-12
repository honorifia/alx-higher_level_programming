#!/usr/bin/python3
"""Defines a text file-reading function"""


def read_file(filename=""):
    """Print the contents of a UTF-8 text file to stdout"""
    with open(filename, encoding="utf-8") as file1:
        print(file1.read(), end="")
