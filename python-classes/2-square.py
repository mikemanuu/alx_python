#!/usr/bin/python3

class Square:

    """
    A class Square that defines a square by:
    Private instance attribute: size

    """

    def __init__(self, size=0):
        self.__size = size

        '''check if size is integer'''
        if not isinstance(size, int):
            raise TypeError('size must be an integer')

        ''' check if size is greater than 0 '''

        if size < 0:
            raise ValueError('size must be >= 0')

    def area(self):
        ''' Returns the current area '''

        return(self.__size * self.__size)
