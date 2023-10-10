#!/usr/bin/python3
"""Defines an empty class BaseGeometry."""


class BaseGeometryMetaClass(type):
    """ Class to override the init subclass in base geometry class. """
    def __dir__(cls):
        attributes = super().__dir__()
        return [attributes for attributes in attributes if attributes != '__init_subclass__']


class BaseGeometry(metaclass=BaseGeometryMetaClass):
    """Creates empty class."""

    def __dir__(cls):
        attributes = super().__dir__()
        return [attributes for attributes in attributes if attributes != '__init_subclass__']
