#!/usr/bin/python3
class Student():

    """class to describe students"""

    def __init__(self, first_name, last_name, age):

        """init method"""

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):

        """retieves a dictionary rep of a student instance"""

        stu = {}

        if attrs is None:

            return self.__dict__

        for key in attrs:

            if key in self.__dict__.keys():

                stu[key] = self.__dict__[key]

        return stu
