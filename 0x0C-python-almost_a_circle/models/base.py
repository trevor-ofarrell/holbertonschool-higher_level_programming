
#!/usr/bin/python3
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

        """static method to return the JSON string representation of list_dictionaries"""

        if list_dictionaries is None or not list_dictionaries:

            return "[]"

        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):

        """class method to save the JSON string representation of list_objs to a file"""
        
        i = 1
        dictionary = {}
        jsondict = {}

        if list_objs is None:
            
            json.dump(dictionary, f)

        with open(cls.__name__ + '.json', mode='w+') as f:

            f.write('[')

            for ele in list_objs:

                f.write(Base.to_json_string(ele.to_dictionary()))
                f.write(', ' if i < len(list_objs) else '')
                i += 1

            f.write(']')
