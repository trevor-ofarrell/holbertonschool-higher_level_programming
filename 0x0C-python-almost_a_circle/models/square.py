#!/usr/bin/python3
from models.rectangle import Rectangle

class Square(Rectangle):

    """class to represent a square, based off of Rectangle"""

    def __init__(self, size, x=0, y=0, id=None):

        """initialization method"""

        super().__init__(size, size, x, y, id)

    def __str__(self):

        return "[{}] ({}) {}/{} - {}".format("Square", self.id, self.x, self.y, self.width)
