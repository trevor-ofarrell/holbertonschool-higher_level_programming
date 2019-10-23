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

    def setUp(self):
        """Resets nb_objects"""
        Base._Base__nb_objects = 0

    def test_error_raises(self):
        """testing type errors and value errors"""

        self.assertRaises((ValueError, TypeError), Rectangle, -1, 0, 'guh', -2)
        self.assertRaises(TypeError, Rectangle, 's', 8.0, (9, 0), ['ew', 'we'])
        self.assertRaises(ValueError, Rectangle, -4, 0, -4, 0, -6)
        self.assertRaises(TypeError, Rectangle, 9, 'dfd')
        self.assertRaises(TypeError, Rectangle, 9, 7, 8, 'fff')
        self.assertRaises(TypeError, Rectangle)
        self.assertRaises(TypeError, Rectangle, 9, 9, 9, 9, 9, 9, 9, 9, 9)
        self.assertRaises(TypeError, Rectangle, str, float, tuple, dict, list)
        self.assertRaises(ValueError, Square, -1, 0, 'guh', -2)
        self.assertRaises(TypeError, Square, str, float)
        self.assertRaises(TypeError, Square, float, tuple, dict, list)
        self.assertRaises(TypeError, Square, tuple, dict, list)
        self.assertRaises(TypeError, Square, dict, list)
        self.assertRaises(TypeError, Square, list, str, float, int)
        self.assertRaises(TypeError, Rectangle, str, float, tuple, dict, list)
        self.assertRaises(TypeError, Rectangle, float, tuple, dict, list)
        self.assertRaises(TypeError, Rectangle, tuple, dict, list)
        self.assertRaises(TypeError, Rectangle, dict, list)
        self.assertRaises(TypeError, Rectangle, list, str, float, int)

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

    def test_id(self):
        """Prints id"""
        r1 = Rectangle(4, 9)
        self.assertEqual(r1.id, 1)

        r2 = Rectangle(9, 4)
        self.assertEqual(r2.id, 2)

        r3 = Rectangle(3, 4, 9, 0, 5)
        self.assertEqual(r3.id, 5)
        self.assertTrue(type(r3), Rectangle)

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

    def test_check_y_TypeError_(self):
        """Test TypeError for y in Rectangle"""
        self.assertRaisesRegex(
            ValueError,
            'y must be >= 0',
            Rectangle,
            4, 2, 0, -6, 12
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

    def test_update(self):
        """Test update method"""
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

    def test_update_extra(self):
        """Update with extra parameters"""
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

    def test_update_no_param(self):
        """Update with extra parameters"""
        output = StringIO()
        sys.stdout = output
        r1 = Rectangle(10, 10, 10, 10)
        r1.update()
        print(r1)
        sys.stdout = sys.__stdout__
        assert output.getvalue() == "[Rectangle] (1) 10/10 - 10/10\n"

    def test_kwargs(self):
        """Test kwargs"""
        output = StringIO()
        sys.stdout = output
        r1 = Rectangle(10, 10, 10, 10)
        r1.update(x=1, height=2, y=3, width=4)
        print(r1)
        sys.stdout = sys.__stdout__
        assert output.getvalue() == "[Rectangle] (1) 1/3 - 4/2\n"

    def test_kwargs_extra_keys(self):
        """Test kwargs with extra parameters"""
        output = StringIO()
        sys.stdout = output
        r1 = Rectangle(10, 10, 10, 10)
        r1.update(x=1, height=2, y=3, width=4, banu=89)
        print(r1)
        sys.stdout = sys.__stdout__
        assert output.getvalue() == "[Rectangle] (1) 1/3 - 4/2\n"

    def test_one_param(self):
        """Passing one parameter"""
        with self.assertRaises(TypeError):
            r1 = Rectangle(4)

    def test_all_param(self):
        """Passing all parameters"""
        r1 = Rectangle(1, 2, 3, 4, 5)

    def test_unknown(self):
        """unknown parameter"""
        with self.assertRaises(NameError):
            r1 = Rectangle(a)

    def test_display(self):
        """Tests rectangle output"""
        output = StringIO()
        sys.stdout = output
        r1 = Rectangle(3, 3)
        r1.display()
        sys.stdout = sys.__stdout__
        assert output.getvalue() == "###\n###\n###\n"

    def test_to_dict_rep_update(self):
        """Testing dictionary update"""
        output = StringIO()
        sys.stdout = output
        r1 = Rectangle(10, 2, 1, 9)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle(1, 1)
        r2.update(**r1_dictionary)
        print(r2)
        sys.stdout = sys.__stdout__
        self.assertEqual(output.getvalue(), "[Rectangle] (1) 1/9 - 10/2\n")

    def test_display_x_y(self):
        """Tests rectangle with x and y"""
        output = StringIO()
        sys.stdout = output
        r2 = Rectangle(3, 2, 1, 0)
        r2.display()
        sys.stdout = sys.__stdout__
        assert output.getvalue() == " ###\n ###\n"

    def test_to_dict_rep(self):
        """Test dictionary"""
        r1 = Rectangle(10, 2, 1, 9)
        r1_dictionary = r1.to_dictionary()
        self.assertEqual(r1_dictionary, {
            'x': 1, 'y': 9, 'id': 1, 'height': 2, 'width': 10})

if __name__ == '__main__':
    unittest.main()
