#!/usr/bin/python3
"""unit test suite"""
import os.path
import unittest
from models.base import Base
from models.square import Square
from models.rectangle import Rectangle

class Test_Rectangle(unittest.TestCase):

      """class to carry out unit tests on Base class"""

      def test_error_raises(self):
            """testing type errors and value errors"""

            self.assertRaises((ValueError, TypeError), Rectangle, -1, 0, 'guh', -2)
            self.assertRaises(TypeError, Rectangle, 'ss', 8.00, (9, 0), ['ewrrew', 'wewe'])
            self.assertRaises(ValueError, Rectangle, -4, 0, -4, 0, -6)
            self.assertRaises(TypeError, Rectangle, str, float, tuple, dict, list)
            self.assertRaises(ValueError, Square, -1, 0, 'guh', -2)
            self.assertRaises(TypeError, Square, str, float, tuple, dict, list)

      def test_rec_area(self):
            """test area method"""
            
            r = Rectangle(5, 6, 0, 0, self.id)
            self.assertEqual(r.area(), 30)

      def test_rec_disply(self):
            """test printing method"""

            r = Rectangle(6, 6, 3, 3)
            self.assertEqual(type(r.__str__()), str)
