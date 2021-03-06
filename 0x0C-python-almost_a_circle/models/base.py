#!/usr/bin/python3
"""base module for holberton school project"""
import json


class Base:

    """base class for project"""

    __nb_objects = 0

    def __init__(self, id=None):

        """initialization method"""

        if id is not None:
            self.id = id

        else:

            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):

        """static method to return the JSON string
           representation of list_dictionaries"""

        if list_dictionaries is None or not list_dictionaries:

            return "[]"

        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):

        """class method to save the JSON string
           representation of list_objs to a file"""

        i = 1
        empty = []

        with open(cls.__name__ + '.json', mode='w') as f:

            if list_objs is None:

                json.dump(empty, f)
                return

            f.write('[')

            for ele in list_objs:

                f.write(Base.to_json_string(ele.to_dictionary()))
                f.write(', ' if i < len(list_objs) else '')
                i += 1

            f.write(']')

    @staticmethod
    def from_json_string(json_string):

        """method to return list of JSON str representations"""

        empty = []

        if json_string is None or not json_string:

            return empty

        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):

        """method to return a instance with attrs already set"""

        if cls.__name__ is 'Square':

            dummy = cls(size=9)

        else:

            dummy = cls(width=9, height=9)

        dummy.update(**dictionary)

        return dummy

    @classmethod
    def load_from_file(cls):

        """method to return list of instances"""

        ret = []

        try:

            with open(cls.__name__ + '.json', mode='r') as f:

                buf = cls.from_json_string(f.read())

                for elm in buf:
                    ret.append(cls.create(**elm))
                return ret

        except FileNotFoundError:

            ret = []

            return ret
