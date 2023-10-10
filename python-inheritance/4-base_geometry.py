#!/usr/bin/python3

"""Defines a base geometry class BaseGeometry."""


class BaseGeometry:
    """Represent base geometry."""

    def __dir__(cls):
        attributes = super().__dir__()
        return [attributes for attributes in attributes if attributes != '__init_subclass__']

    def area(self):
        """ Area not implemented. """
        raise Exception("area() is not implemented")
