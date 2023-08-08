#!/usr/bin/python3

"""Defines a base geometry class BaseGeometry."""


class BaseGeometry:
    """Represent base geometry."""

    def area(self):
        """Not implemented."""
        raise Exception("area() is not implemented")

    def __dir__(self):
        return sorted(dir(type(self)) + list(self.__dict__) + ['area'] + ['area'])
