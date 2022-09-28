#!/usr/bin/python3
"""
append_write module
"""


def append_write(filename="", text=""):
    """
    write_file - 
    Args:
        filename: name of the file
        text: text to be written
    Return: number of bytes written.
    """
    with open(filename, mode="a", encoding="UTF-8") as f:
        return (f.write(text))
