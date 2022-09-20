#!/usr/bin/python3
"""
LockedClass class
"""


class LockedClass:
    """ setattr """
    def __setattr__(self, atr, value):
        if atr == "first_name":
            self.__dict__[atr] = value
        else:
            raise AttributeError("'LockedClass' object has no attribute '" + atr + "'")
