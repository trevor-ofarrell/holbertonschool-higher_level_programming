#!/usr/bin/python3
class Student():

    """class to describe students"""

    first_name = ""
    last_name = ""
    age = 0

    def __init__(self, first_name, last_name, age):

        """init method"""

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):

        """retieves a dictionary rep of a student instance"""

        stu = Student(self.first_name, self.last_name, self.age).__dict__

        return stu
