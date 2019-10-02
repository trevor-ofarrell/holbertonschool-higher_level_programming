#!/usr/bin/python3
class Square:
    """ class to represent a square"""

    def __init__(self, size=0, position=(0, 0)):

        """init method

        Attributes:

           attr1 (size) - size of square
           attr2 (position) - orientation of square

        Raises:

           ValueError:  If size is negitive
           TypeError:  If size is not an int"""

        self.size = size
        self.position = position

    @property
    def size(self):
        """property getter"""
        return self.__size

    @size.setter
    def size(self, value):
        """property setter"""
        if isinstance(value, str) is True:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """property getter for position of square"""
        return self.__position

    @position.setter
    def position(self, value):
        """position setter for square"""

        if isinstance(value, tuple) is False:
            raise TypeError("position must be a tuple of 2 positive integers")
        if isinstance(value[0], int) is False:
            raise TypeError("position must be a tuple of 2 positive integers")
        if isinstance(value[1], int) is False:
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        if len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def my_print(self):
        """Public instance method to print square based on area data"""
        if self.size == 0:
            print("")
        else:
            print('\n' * self.position[1], end="")
            for i in range(self.size):
                print(" " * self.position[0], end="")
                print("#" * self.size)
                print("")

    def area(self):
        """Public instance method to return area of square"""
        return self.__size ** 2
