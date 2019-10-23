#!/usr/bin/python3
"""Unittest for Square Size
"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestSquareSize(unittest.TestCase):

    """Test Square Size Method"""

    def test_str_method(self):
        """test str method for square"""
        s1 = Square(5)
        self.assertEqual(str(s1), "[Square] (40) 0/0 - 5")

    def test_to_dictionary(self):
        """Test conversion to dictionary"""
        r = Square(1, 1, 1, 1)
        d = {'id': 1, 'size': 1, 'x': 1, 'y': 1}
        self.assertEqual(r.to_dictionary(), d)
        r.my_fun_new_attr = 42
        self.assertEqual(r.to_dictionary(), d)
