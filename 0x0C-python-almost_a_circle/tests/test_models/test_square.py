#!/usr/bin/python3
"""Unittest for Square Size"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
import sys
from io import StringIO


class Test_Square(unittest.TestCase):

    """class to test square class/methods"""

    def setUp(self):
        """Resets nb_objects"""
        Base._Base__nb_objects = 0

    def test_id(self):
        """test instance count"""
        new = Square(9)
        self.assertEqual(new.id, 1)

    def test_parameters(self):
        """Extra parameters"""
        with self.assertRaises(TypeError):
            r1 = Square("string")
        with self.assertRaises(TypeError):
            r1 = Square(1, "2")
        with self.assertRaises(TypeError):
            r1 = Square(1.2)
        with self.assertRaises(TypeError):
            r1 = Square(1, 2, 3, 4, 1, 3)
        with self.assertRaises(NameError):
            r1 = Square(a)
        with self.assertRaises(TypeError):
            r1 = Square(None)
        with self.assertRaises(TypeError):
            r1 = Square()
        with self.assertRaises(ValueError):
            r1 = Square(0)
        with self.assertRaises(ValueError):
            r1 = Square(-1)
        with self.assertRaises(ValueError):
            r1 = Square(1, -1, 2, 3)
        with self.assertRaises(ValueError):
            r1 = Square(1, 2, -3)

    def test_area(self):
        """Print area"""
        r1 = Square(10)
        self.assertTrue(type(r1), Square)

    def test_display(self):
        """rectangle output"""
        output = StringIO()
        sys.stdout = output
        r1 = Square(2)
        r1.display()
        sys.stdout = sys.__stdout__
        assert output.getvalue() == "##\n##\n"

    def test_display_x_y(self):
        """rectangle with x and y"""
        output = StringIO()
        sys.stdout = output
        r2 = Square(2, 1, 0)
        r2.display()
        sys.stdout = sys.__stdout__
        assert output.getvalue() == " ##\n ##\n"

    def test_update(self):
        """update"""
        output = StringIO()
        sys.stdout = output
        r1 = Square(10, 10, 10)
        r1.update(89)
        r1.update(89, 2)
        r1.update(89, 2, 3)
        r1.update(89, 2, 3, 4)
        print(r1)
        sys.stdout = sys.__stdout__
        assert output.getvalue() == "[Square] (89) 3/4 - 2\n"

    def test_update_extra(self):
        """Update with extra parameters"""
        output = StringIO()
        sys.stdout = output
        r1 = Square(10, 10, 10)
        r1.update(89, 3, 4, 5, 6)
        print(r1)
        sys.stdout = sys.__stdout__
        assert output.getvalue() == "[Square] (89) 4/5 - 3\n"

    def test_kwargs_extra_keys(self):
        """kwargs normal behavior"""
        output = StringIO()
        sys.stdout = output
        r1 = Square(2, 2, 2, 2)
        r1.update(id=1, x=1, size=2, y=3, banu=89)
        print(r1)
        sys.stdout = sys.__stdout__
        assert output.getvalue() == "[Square] (1) 1/3 - 2\n"

    def test_to_dictionary(self):
        """to dictionary"""
        s1 = Square(10, 2, 1)
        s1_dictionary = s1.to_dictionary()
        self.assertEqual(s1_dictionary, {'id': 1, 'x': 2, 'size': 10, 'y': 1})
        self.assertTrue(type(s1_dictionary), dict)

    def test_str_method(self):
        """test str method for square"""
        s1 = Square(5)
        self.assertEqual(str(s1), "[Square] (1) 0/0 - 5")

    def test_to_dictionary2(self):
        """Test conversion to dictionary"""
        r = Square(1, 1, 1, 1)
        d = {'id': 1, 'size': 1, 'x': 1, 'y': 1}
        self.assertEqual(r.to_dictionary(), d)
        r.my_fun_new_attr = 42
        self.assertEqual(r.to_dictionary(), d)

    def test_save_to_file_None2(self):
        """JSON string None"""
        Square.save_to_file(None)
        with open("Square.json") as file:
            self.assertEqual(file.read(), "[]")

if __name__ == '__main__':
    unittest.main()
