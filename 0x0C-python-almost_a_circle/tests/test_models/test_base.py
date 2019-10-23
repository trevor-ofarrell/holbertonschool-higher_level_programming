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
        """test type of id"""
        test = Base()
        self.assertEqual(type(test.id), int)

    def test_id_greater_than_zero(self):
        """test id value"""
        test = Base()
        self.assertEqual(test.id > 0, True)

    def test_to_json_string(self):
        """test return type"""
        r = Rectangle(10, 5, 5, 5)
        testd = r.to_dictionary()
        jdict = Base.to_json_string([testd])
        self.assertEqual(type(jdict), str)

    def test_to_json_string_none(self):
        """test empty string"""
        jsonstr = None
        Base.to_json_string(jsonstr)
        self.assertEqual(jsonstr, None)

    def test_save_to_file_null(self):
        """test if file exists"""
        lo = None
        Base.save_to_file(lo)
        self.assertEqual(os.path.exists('Base.json'), True)

    def test_save_to_file_data_type(self):
        """test type of files content"""
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])
        with open("Rectangle.json", "r") as file:
            data = file.read()
        self.assertEqual(type(data), str)

    def test_save_to_file_empty_contents(self):
        """test saving empty list to file"""
        lo = None
        Base.save_to_file(lo)
        with open("Base.json", mode='r') as f:
            data = f.read()
        self.assertEqual(data, '[]')

    def test_from_json_string_none(self):
        """test submitting None"""
        lo = None
        jsonstr = Base.from_json_string(lo)
        self.assertEqual(jsonstr, None or [])

    def test_from_json_string_data_type(self):
        """test return type"""
        list_input = [
            {'id': 89, 'width': 10, 'height': 4},
            {'id': 7, 'width': 1, 'height': 7}
        ]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertEqual(type(list_output), list)

    def test_create_instance(self):
        """test intance creation"""
        r1 = Rectangle(3, 5, 1)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertEqual(isinstance(r2, Base), True)

    def test_create_class_name(self):
        """comparison of instances"""
        r1 = Rectangle(3, 5, 1)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertEqual(r1 is r2 and r1 == r2, False)

    def test_load_from_file(self):
        """Test load_from_file method"""

        r1 = Rectangle(3, 5, 2, 4, 1)
        dr1 = r1.to_dictionary()
        r2 = Rectangle(3, 5, 2, 4)
        dr2 = r2.to_dictionary()
        r3 = Rectangle(3, 10)
        dr3 = r3.to_dictionary()
        s1 = Square(3, 2, 4, 1)
        ds1 = s1.to_dictionary()
        s2 = Square(3, 2, 4)
        ds2 = s2.to_dictionary()
        s3 = Square(3)
        ds3 = s3.to_dictionary()

        Rectangle.save_to_file([r1, r2, r3])
        list_objs_r = Rectangle.load_from_file()
        Square.save_to_file([s1, s2, s3])
        list_objs_s = Square.load_from_file()

        self.assertIsInstance(list_objs_r[0], Rectangle)
        self.assertDictEqual(list_objs_r[0].to_dictionary(), dr1)

        self.assertIsInstance(list_objs_r[1], Rectangle)
        self.assertDictEqual(list_objs_r[1].to_dictionary(), dr2)

        self.assertIsInstance(list_objs_r[2], Rectangle)
        self.assertDictEqual(list_objs_r[2].to_dictionary(), dr3)

        self.assertIsInstance(list_objs_s[0], Square)
        self.assertDictEqual(list_objs_s[0].to_dictionary(), ds1)

        self.assertIsInstance(list_objs_s[1], Square)
        self.assertDictEqual(list_objs_s[1].to_dictionary(), ds2)

        self.assertIsInstance(list_objs_s[2], Square)
        self.assertDictEqual(list_objs_s[2].to_dictionary(), ds3)

    def test_create(self):
        """Test instantiation via Create method"""

        dr1 = {'id': 1, 'width': 3, 'height': 5, 'x': 2, 'y': 4}
        r1 = Rectangle.create(**dr1)
        self.assertEqual(r1.to_dictionary(), dr1)
        self.assertEqual(Base._Base__nb_objects, 1)

        ds1 = {'id': 1, 'size': 3, 'x': 2, 'y': 4}
        s1 = Square.create(**ds1)
        self.assertEqual(s1.to_dictionary(), ds1)
        self.assertEqual(Base._Base__nb_objects, 2)

        r2 = Rectangle(3, 5, 2, 4, 1)
        dr2 = r2.to_dictionary()
        r3 = Rectangle.create(**dr2)
        self.assertEqual(r3.to_dictionary(), dr2)
        self.assertEqual(Base._Base__nb_objects, 3)

        r4 = Rectangle(3, 5, 2, 4)
        dr4 = r4.to_dictionary()
        r5 = Rectangle.create(**dr4)
        self.assertEqual(r5.to_dictionary(), dr4)
        self.assertEqual(Base._Base__nb_objects, 5)

        r6 = Rectangle(3, 5)
        dr6 = r6.to_dictionary()
        r7 = Rectangle.create(**dr6)
        self.assertEqual(r7.to_dictionary(), dr6)
        self.assertEqual(Base._Base__nb_objects, 7)

        s2 = Square(3, 2, 4, 1)
        ds2 = s2.to_dictionary()
        s3 = Square.create(**ds2)
        self.assertEqual(s3.to_dictionary(), ds2)
        self.assertEqual(Base._Base__nb_objects, 8)

        s4 = Square(3, 2, 4)
        ds4 = s4.to_dictionary()
        s5 = Square.create(**ds4)
        self.assertEqual(s5.to_dictionary(), ds4)
        self.assertEqual(Base._Base__nb_objects, 10)

        s6 = Square(3, 2)
        ds6 = s6.to_dictionary()
        s7 = Square.create(**ds6)
        self.assertEqual(s7.to_dictionary(), ds6)
        self.assertEqual(Base._Base__nb_objects, 12)
