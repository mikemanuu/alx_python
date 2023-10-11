#!/usr/bin/python3

"""Defines a class Rectangle that inherits from BaseGeometry."""

BaseGeometry = __import__('5-base_geometry').BaseGeometry


class CustomDirMeta(type):
    def __dir__(cls):
        desired_attributes = ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__le__', '__lt__',
                              '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'area', 'integer_validator']
        return desired_attributes


class Rectangle(BaseGeometry, metaclass=CustomDirMeta):
    """ Represent a rectangle using Base Geometry. """

    def __init__(self, width, height):
        """Intialize a new Rectangle.

        Args:
            width (int): The width of the new Rectangle.
            height (int): The height of the new Rectangle.
        """
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def area(self):
        """Calculates the area of the rectangle"""

        return self.__width * self.__height

    def __str__(self):
        """ Retutn print() and str() representation of rectangle. """
        string = "[" + str(self.__class__.__name__) + "]"
        string += str(self.__width) + "," + str(self.__height)
        return string
