#!/usr/bin/python3
class Square:
    """ class to represent a square"""
    pass

    """init method
       Attributes:
        attr1 (:obj - size) size of square"""

    def __init__(self, size=0):
        self.__size = size
        if isinstance(size, int) is False:
            try:
                raise TypeError("size must be an integer")
            except NameError:
                raise
        if size < 0:
            try:
                raise ValueError("size must be >= 0")
            except ValueError:
                raise
