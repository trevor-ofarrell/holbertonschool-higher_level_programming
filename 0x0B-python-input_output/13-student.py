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

    def to_json(self, attrs=None):

        """retieves a dictionary rep of a student instance"""

        stu = {}

        if not attrs:

            return self.__dict__

        for key, value in self.__dict__.items():

            if key in attrs and all(isinstance(key, str) for key in attrs):

                stu[key] = value

        return stu

    def reload_from_json(self, json):

        """replaces all class atributes with JSON representation"""

        for (key, value) in json.items():

            setattr(self, key, value)

        return self.__dict__
