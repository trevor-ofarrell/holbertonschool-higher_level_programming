#!/usr/bin/python3
"""unit test suite"""
import os.path
import unittest
from models.base import Base
from models.square import Square
from models.rectangle import Rectangle
from io import StringIO
import sys


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
            
      def test_check_width(self):
            """Test width set of rectangle"""
            r1 = Rectangle(10, 2)
            self.assertEqual(r1.width, 10)

            r2 = Rectangle(2, 10)
            self.assertEqual(r2.width, 2)

            r3 = Rectangle(5, 2, 0, 0, 12)
            self.assertEqual(r3.width, 5)

      def test_check_x(self):
            """Test x of rectangle"""
            r1 = Rectangle(10, 2)
            self.assertEqual(r1.x, 0)

            r2 = Rectangle(2, 10, 6)
            self.assertEqual(r2.x, 6)

            r3 = Rectangle(5, 2, 3, 9, 12)
            self.assertEqual(r3.x, 3)

            r4 = Rectangle(5, 2, 0, 3, 12)
            self.assertEqual(r4.x, 0)

      def test_check_x_TypeError_02(self):
            """Test TypeError for x in Rectangle"""
            self.assertRaisesRegex(
                  TypeError,
                  'x must be an integer',
                  Rectangle,
                  4, 2, [1, 2, 3, 4], 0, 12
            )

      def test_check_x_ValueError(self):
            """Test ValueError for x in Rectangle"""
            self.assertRaisesRegex(
                  ValueError,
                  'x must be >= 0',
                  Rectangle,
                  4, 2, -1, 0, 12
            )

      def test_check_y(self):
            """Test y of rectangle"""
            r1 = Rectangle(10, 2)
            self.assertEqual(r1.y, 0)

            r2 = Rectangle(2, 10, 6, 4)
            self.assertEqual(r2.y, 4)

            r3 = Rectangle(5, 2, 3, 9, 12)
            self.assertEqual(r3.y, 9)

            r4 = Rectangle(5, 2, 3, 0, 12)
            self.assertEqual(r4.y, 0)

      def test_check_y_TypeError_01(self):
            """Test TypeError for y in Rectangle"""
            self.assertRaisesRegex(
                  TypeError,
                  'y must be an integer',
                  Rectangle,
                  4, 2, 0, 'string', 12
            )

      def test_check_y_TypeError_02(self):
            """Test TypeError for y in Rectangle"""
            self.assertRaisesRegex(
                  TypeError,
                  'y must be an integer',
                  Rectangle,
                  4, 2, 0, [1, 2, 3, 4], 12
            )

      def test_check_y_TypeError_(self):
            """Test TypeError for y in Rectangle"""
            self.assertRaisesRegex(
                  ValueError,
                  'y must be >= 0',
                  Rectangle,
                  4, 2, 0, -6, 12
            )
   
      def test_update(self):
            """Test update"""
            output = StringIO()
            sys.stdout = output
            r1 = Rectangle(10, 10, 10, 10)
            r1.update(89)
            r1.update(89, 2)
            r1.update(89, 2, 3)
            r1.update(89, 2, 3, 4)
            r1.update(89, 2, 3, 4, 5)
            print(r1)
            sys.stdout = sys.__stdout__
            assert output.getvalue() == "[Rectangle] (89) 4/5 - 2/3\n"
