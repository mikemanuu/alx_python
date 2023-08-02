#!/usr/bin/python3
""" Module Square """


class Square:

    """
    A class Square that defines a square by:
    Private instance attribute: size
    """

    def __init__(self, size=0):
        self.__size = size

        if not isinstance(size, int):
            raise TypeError('size must be an integer')

        if size < 0:
            raise ValueError('size must be >= 0')
