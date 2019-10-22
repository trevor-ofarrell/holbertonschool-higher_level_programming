#!/usr/bin/python3                                                              
import os.path
import unittest
from models.base import Base
from models.rectangle import Rectangle

class Test_Base(unittest.TestCase):

    """class to carry out unit tests on Base class"""

    def test_id(self):

        test = Base()
        self.assertEqual(test.id, 1)

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

    def test_save_to_file(self):

        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])
        with open("Rectangle.json", "r") as file:
            data = file.read()
        self.assertEqual(type(data), str)

    def test_save_to_file_empty_list(self):

        lo = None
        Base.save_to_file(lo)
        self.assertEqual(os.path.exists('Base.json'), True)

    def test_save_to_file_null_file(self):

        lo = None
        Base.save_to_file(lo)
        with open("Base.json", mode='r') as f:
            data = f.read()
        self.assertEqual(data, '[]')
