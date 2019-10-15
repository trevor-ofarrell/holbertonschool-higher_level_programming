#!/usr/bin/python3
class BaseGeometry():


    def area(self):

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):

        if not isinstance(value, int):

            raise TypeError("{} {}".format(name, "must be an integer"))

        if value <= 0:

            raise ValueError("{} {}".format(name, "must be greater than 0"))
