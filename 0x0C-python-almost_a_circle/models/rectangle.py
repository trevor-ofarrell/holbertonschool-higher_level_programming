#!/usr/bin/python3
import sys
from models.base import Base
class Rectangle(Base):
    
    """class that represents a rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):

        """initialization method"""

        self.width = width
        self.height = height
        self.x = x
        self.y = y

        super().__init__(id)
        

    @property
    def width(self):

        """getter method"""

        return self.__width

    @width.setter
    def width(self, value):

        """width setter method"""

        if type(value) is not int:

            raise TypeError("width must be an integer")

        if value <= 0:

            raise ValueError("width must be > 0")

        self.__width = value

    @property
    def height(self):

        """getter method"""

        return self.__height

    @height.setter
    def height(self, value):

        """height setter method"""

        if type(value) is not int:

            raise TypeError("height must be an integer")

        if value <= 0:

            raise ValueError("height must be > 0")
        
        self.__height = value

    @property
    def x(self):

        """getter method"""

        return self.__x

    @x.setter
    def x(self, value):

        """setter method"""

        if type(value) is not int:

            raise TypeError("x must be an integer")

        if value < 0:

            raise ValueError("x must be >= 0")
        
        self.__x = value
    
    @property
    def y(self):

        """getter method"""

        return self.__y

    @y.setter
    def y(self, value):

        """setter method"""

        if type(value) is not int:

            raise TypeError("y must be an integer")

        if value < 0:

            raise ValueError("y must be >= 0")
        
        self.__y = value

    def area(self):

        """public method to return area of rectangle"""

        return self.__width * self.__height

    def display(self):

        sym = '#'
        l = []

        """public method to print str representation of the rectangle"""

        print(self.__y * '\n' + (self.__x * ' ' + '#' * self.__width + '\n') * self.__height, end='')

    def __str__(self):

        """overriding str method"""

        return "[{}] ({}) {}/{} - {}/{}".format("Rectangle", self.id, self.x, self.y, self.__width, self.__height)

    def update(self, *args, **kwargs):

        """public method to assign an argument to each attr"""
    
        if args:

            try:

                if len(args) == 1:
                    setattr(self, 'id', args[0])
                if len(args) == 2:
                    setattr(self, 'width', args[1])
                if len(args) == 3:
                    setattr(self, 'height', args[2])
                if len(args) == 4:
                    setattr(self, 'x', args[3])
                if len(args) == 5:
                    setattr(self, 'y', args[4])

            except Exception:
            
                raise Exception

        else:

            for key, value in kwargs.items():
                setattr(self, key, value)
                
