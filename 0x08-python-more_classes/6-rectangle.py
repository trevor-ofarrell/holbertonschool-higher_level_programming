#!/usr/bin/python3
class Rectangle:

    """class to represent a rectangle"""

    number_of_instances = 0

    def __init__(self, width=0, height=0):

        """initalization method
        Attributes:
            attr1 (width)
            attr2 (height)
        """

        self.width = width
        self.height = height

        type(self).number_of_instances += 1

    @property
    def width(self):

        """property getter"""

        return self.__width

    @width.setter
    def width(self, value):

        """property setter"""

        if not isinstance(value, int):
            raise TypeError("width must be an integer")

        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self):

        """property getter"""

        return self.__height

    @height.setter
    def height(self, value):

        """property setter"""

        if not isinstance(value, int):
            raise TypeError("height must be an integer")

        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value

    def area(self):

        """return the area of rectangle"""

        return self.width * self.height

    def __str__(self):

        if self.height == 0 or self.width == 0:
            return ""

        str1 = (self.width * "#" + '\n') * self.height

        return str1[:-1]

    def __repr__(self):

        return "Rectangle(%s, %s)" % (self.height, self.width)

    def perimeter(self):

        """return perimeter of retangle"""

        if self.width == 0 or self.height == 0:
            return 0

        perm = (self.height + self.width) * 2

        return perm

    def __del__(self):

        """deletion method"""

        print("Bye rectangle...")

        type(self).number_of_instances -= 1
