#!/usr/bin/python3
""" Module Square """


class square:

    """
    A class Square that defines a square by:
        Private instance attribute: size.
    returns:
        Private attribute size
    """

    def __init__(self, size=0):
        """ Constructor method for the Square class """
        self.__size = size

    @property
    def size(self):
        ''' Retrieves private property size '''

        return self.__size

    @size.setter
    def size(self, value):
        '''property setter'''

        '''check if size is integer'''
        if not isinstance(value, int):
            raise('size must be an integer')

        ''' check if size is greater than 0 '''
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def area(self):
        ''' Returns the current area '''

        return(self.__size * self.__size)
