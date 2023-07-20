#!/usr/bin/python3
""" defines a square class """


class Square:
    """ defines a square """
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    @property
    def size(self):
        return (self.__size)

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        return (self.__position)

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                type(value[0]) is not int or
                type(value[1]) is not int):
            raise TypeError("size must be an integer")
        self.__position = value

    def area(self):
        return self.__size ** 2

    def my_print(self):
        for i in range(self.position[1]):
            print()
        for i in range(self.size):
            if i > 0:
                print()
            for j in range(self.position[0]):
                print(" ", end="")
            for j in range(self.size):
                print("#", end="")
        print()
