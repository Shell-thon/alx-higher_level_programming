#!/usr/bin/python3
""" define a class Square """


class Square:
    """ define __init__ function """
    def __init__(self, size=0, position=(0, 0)):
        """ initializes size of self with size """
        self.size = size
        self.position = position

    @property
    def size(self):
        """ returns __size of self """
        return self.__size

    @size.setter
    def size(self, value):
        """ if statement """
        if type(value) is not int:
            """ raise error """
            raise TypeError("size must be an integer")
        elif value < 0:
            """ raise error """
            raise ValueError("size must be >= 0")
        else:
            """ initialize """
            self.__size = value
    """ defines area function """
    def area(self):
        """ returns area """
        return self.__size ** 2
    """ defines my_print function """
    def my_print(self):
        if self.__size == 0:
            print()
        for y in range(0, self.__position[1]):
            print()
        for i in range(0, self.__size):
            for x in range(0, self.__position[0]):
                print(" ", end="")
            for j in range(0, self.__size):
                print("#", end="")
            print()

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if type(value) is not tuple or len(value) != 2 or \
           type(value[0]) is not int or value[0] < 0 or \
           type(value[1]) is not int or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value
