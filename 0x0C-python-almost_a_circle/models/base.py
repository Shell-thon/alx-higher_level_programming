#!/usr/bin/python3
"""
base module
"""
import json
import os


class Base:
    """
    Base implementation
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        init - initialization
        Args:
            id: object id
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def to_json_string(list_dictionaries):
        """
        to_json_string - returns the JSON string representation of list_dictionaries.
        Args:
            list_dictionaries: is a list of dictionaries
        """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        else:
            return json.dumps(list_dictionaries)
