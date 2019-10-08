#!/usr/bin/python3
class Square:
    """ class to represent a square"""

    def __init__(self, size=0):

        """init method
        Attributes:
        attr1 (:obj - size) size of square
        Raises:
        ValueError: If size is negitive
        TypeError: If size is not an int"""

        self.__size = size
        self.size = size
        if size < 0:
            try:
                raise ValueError("size must be >= 0")
            except ValueError:
                raise

    def area(self):
        """Public instance method to return area of square"""
        if isinstance(self.size, str) is True:
            raise TypeError("size must be an integer")
        return self.size ** 2
