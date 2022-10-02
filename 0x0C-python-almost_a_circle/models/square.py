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

    def __str__(self):
        """
        overriden __str__ method
        """
        return "[Square] ({}) {}/{} - {}".format(
                self.id, self.x, self.y, self.__size)

    @property
    def size(self):
        """ size getter """
        return self.__size

    @size.setter
    def size(self, size):
        """ size setter """
        if not isinstance(size, int):
            raise TypeError("width must be an integer")
        if size <= 0:
            raise ValueError("width must be > 0")
        self.__size = size
        self.__width = self.__height = size

    def update(self, *args, **kwargs):
        """
        assigns attributes
        """
        asa = (self.id, self.size, self.x, self.y)
        if args:
            self.id, self.size, self.x, self.y = \
                    args + asa[len(args):len(asa)]
        elif kwargs:
            for (name, value) in kwargs.items():
                setattr(self, name, value)
