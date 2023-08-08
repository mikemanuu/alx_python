#!/usr/bin/python3
"""Defines an empty class BaseGeometry."""


class BaseGeometry:
    """Represent base geometry."""

    def __init_subclass__(cls):
        pass

    def __dir__(self):
        return[attr for attr in dir(type(self)) if attr != '__init_subclass__']

    def __class__(self):
        return type(self)
