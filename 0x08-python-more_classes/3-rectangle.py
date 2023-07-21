#!/usr/bin/python3
""" empty rectangle class"""


class Rectangle:
    """ empty rectangle class"""
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    def __str__(self):
        res = ""
        for i in range(self.height):
            for j in range(self.width):
                res = res + "#"
            if i != self.height - 1:
                res = res + "\n"
        return res

    @property
    def width(self):
        return (self.__width)

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return (self.__height)

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return self.height * self.width

    def perimeter(self):
        if self.width == 0 or self.height == 0:
            return 0
        return self.width * 2 + self.height * 2
