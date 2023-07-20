#!/usr/bin/python3
""" defines a square class """


class Square:
    """ defines a square """
    def __init__(self, size=0):
        self.size = size

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

    def area(self):
        return self.__size ** 2

    def my_print(self):
        for i in range(self.size):
            if i > 0:
                print()
            for j in range(self.size):
                print("#", end="")
        print()
