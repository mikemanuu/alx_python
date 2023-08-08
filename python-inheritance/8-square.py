#!/usr/bin/python3

"""Defines a Rectangle subclass Square."""

Rectangle = __import__('7-rectangle').Rectangle


class Square(Rectangle):
    """Represent a square."""

    def __init__(self, size):
        """Initialize a new square.

        Args:
            size (int): The size of the new square.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        return "[Square] {}/{}".format(
            self._Rectangle__width,
            self._Rectangle__height
        )
