#!/usr/bin/python3
"""
base module
"""
import json
import os
import csv


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string representation of list_dictionaries.
        Args:
            list_dictionaries: is a list of dictionaries
        """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file.
        Args:
            cls:
            list_objs: is a list of instances who inherits of Base
        """
        if list_objs is None or list_objs == []:
            lst = "[]"
        else:
            lst = cls.to_json_string([o.to_dictionary() for o in list_objs])
        with open(cls.__name__ + ".json", 'w') as f:
            f.write(lst)

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string representation json_string.
        Args:
            json_string: is a string representing a list of dictionaries
        """
        if json_string is None or json_string == []:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set.
        Args:
            dictionary: can be thought of as a double pointer to a dictionary
        """
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        else:
            dummy = cls(1)

        dummy.update(**dictionary)
        return dummy
