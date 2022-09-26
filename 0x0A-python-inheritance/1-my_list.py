#!/usr/bin/python3
"""
MyList is a child of list
"""


class MyList(list):
    """
    print_sorted - prints the list
    """
    def print_sorted(self):
        print(sorted(self))
