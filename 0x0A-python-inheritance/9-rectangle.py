#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):

    """class for rectangles derived from the base geometry superclass"""

    def __init__(self, width, height):

        """init method"""

        self.integer_validator("width", width)
        self.integer_validator("height", height)

        self.__width = width
        self.__height = height

    def area(self):

        """returns area of rectangle"""

        return self.__width * self.__height

    def __str__(self):

        """string representation of the rectangle"""

        return "{} {}/{}".format("[Rectangle]", self.__width, self.__height)
