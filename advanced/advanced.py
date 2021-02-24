"""Functions for use with advanced pytest features."""

import sys


def yo(name):
    """Say yo to yo friend."""
    return f"yo, {name}!"


def blackBox(thing1, thing2, num):
    """Do crazy stuff!"""
    return thing1 * num + thing2


def createList(num):
    """Create a list of numbers"""
    return list(range(0, num))
