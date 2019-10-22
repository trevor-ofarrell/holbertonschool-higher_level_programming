#!/usr/bin/python3
"""module for square class"""
from models.rectangle import Rectangle


class Square(Rectangle):

    """class to represent a square, based off of Rectangle"""

    def __init__(self, size, x=0, y=0, id=None):

        """initialization method"""

        super().__init__(size, size, x, y, id)

    @property
    def size(self):

        """getter for size"""

        return self.width

    @size.setter
    def size(self, value):

        """size setter"""

        self.width = value
        self.height = value

    def __str__(self):

        """method to override str method"""

        return "[{}] ({}) {}/{} - {}".format("Square",
                                             self.id, self.x,
                                             self.y, self.width)

    def update(self, *args, **kwargs):

        """public method to assign an argument to each attr"""

        if args:

            if len(args) >= 0:
                setattr(self, 'id', args[0])
            if len(args) == 2:
                setattr(self, 'size', args[1])
            if len(args) == 3:
                setattr(self, 'x', args[2])
            if len(args) == 4:
                setattr(self, 'y', args[3])

        else:

            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):

        """public method that returns the dictionary
        representation of a Square"""

        return {'id': self.id, 'size': self.size, 'x': self.x, 'y': self.y}
