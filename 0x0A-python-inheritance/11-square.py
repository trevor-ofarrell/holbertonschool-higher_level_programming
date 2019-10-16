#!/usr/bin/python3
Rectangle = __import__('9-rectangle').Rectangle
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Square(Rectangle):

    """class that defines a square, derived from the Rectangle class"""

    def __init__(self, size):

        """init method"""

        self.integer_validator("size", size)

        self.__size = size

        super().__init__(size, size)

    def area(self):

        """method to calculate area of square"""

        return self.__size * self.__size

    def __str__(self):

        """string representation of the rectangle"""

        return "{} {}/{}".format("[Square]", self.__size, self.__size)
