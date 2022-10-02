#!/usr/bin/python3
"""
square module
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Square implementation
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
        init - initilizer
        Args:
            size: size of the square
            x: x position of the square
            y: y position of the square
            id: id of the square
        """
        super().__init__(size, size, x, y, id)
        self.__size = size

    @property
    def size(self):
        """ size getter """
        return self.__size

    @size.setter
    def size(self, size):
        """ size setter """
        self.__width = size
        self.__height = size
