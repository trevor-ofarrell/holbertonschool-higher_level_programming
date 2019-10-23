#!/usr/bin/python3
"""unit test suite"""
import os.path
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square

class Test_Base(unittest.TestCase):

    """class to carry out unit tests on Base class"""

    def test_id(self):

        test = Base()
        self.assertEqual(test.id, 5)

    def test_to_json_string(self):

        r = Rectangle(10, 5, 5, 5)
        testd = r.to_dictionary()
        jdict = Base.to_json_string([testd])
        self.assertEqual(type(jdict), str)

    def test_to_json_string_none(self):

        jsonstr = None
        Base.to_json_string(jsonstr)
        self.assertEqual(jsonstr, None)

    def test_save_to_file_null(self):

        lo = None
        Base.save_to_file(lo)
        self.assertEqual(os.path.exists('Base.json'), True)

    def test_save_to_file_data_type(self):

        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])
        with open("Rectangle.json", "r") as file:
            data = file.read()
        self.assertEqual(type(data), str)

    def test_save_to_file_empty_contents(self):

        lo = None
        Base.save_to_file(lo)
        with open("Base.json", mode='r') as f:
            data = f.read()
        self.assertEqual(data, '[]')

    def test_from_json_string_none(self):

        lo = None
        jsonstr = Base.from_json_string(lo)
        self.assertEqual(jsonstr, None or [])

    def test_from_json_string_data_type(self):

        list_input = [
        {'id': 89, 'width': 10, 'height': 4}, 
        {'id': 7, 'width': 1, 'height': 7}
        ]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertEqual(type(list_output), list)

    def test_create_instance(self):

        r1 = Rectangle(3, 5, 1)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertEqual(isinstance(r2, Base), True)

    def test_create_class_name(self):

        r1 = Rectangle(3, 5, 1)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertEqual(r1 is r2 and r1 == r2, False)
