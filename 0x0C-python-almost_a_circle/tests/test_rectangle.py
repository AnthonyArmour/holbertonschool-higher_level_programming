#!/usr/bin/python3
"""Unit test for rectangle class"""


from models.base import Base
from models.rectangle import Rectangle
import unittest


class RectangleTest(unittest.TestCase):
    """unittest class"""
    def test_base(self):
        result1 = Base(12)
        self.assertEqual(result1.id, 12)

    def test_rectangle(self):
        """rectangle unittest"""
        result = Rectangle(10, 2)
        self.assertEqual(result.width, 10)
        self.assertEqual(result.height, 2)
        with self.assertRaises(TypeError):
            Rectangle(10, "2")
        with self.assertRaises(ValueError):
            Rectangle(10, 2, 3, -1)
        r = Rectangle(10, 2)
        with self.assertRaises(ValueError):
            r.width = -10
        with self.assertRaises(TypeError):
            r.x = {}
        t = Rectangle(10, 2, 3, 4)
        self.assertEqual(t.width, 10)
        self.assertEqual(t.height, 2)
        self.assertEqual(t.x, 3)
        self.assertEqual(t.y, 4)

    def test_area(self):
        """unittest for area method"""
        result2 = Rectangle(10, 2)
        self.assertEqual(result2.area(), 20)
        result2.height = 10
        self.assertEqual(result2.area(), 100)

    def test_str(self):
        """unittest for str method"""
        r1 = Rectangle(4, 6, 2, 1, 12)
        r2 = Rectangle(5, 5, 1)
        self.assertEqual(str(r1), "[Rectangle] (12) 2/1 - 4/6")
        self.assertEqual(str(r2), "[Rectangle] (7) 1/0 - 5/5")

    def test_args_kwargs(self):
        """unittest for *args and **kwargs"""
        r3 = Rectangle(10, 10, 10, 10, 10)
        r3.update(89, 2, 3, 4, 5)
        self.assertEqual(r3.id, 89)
        self.assertEqual(r3.width, 2)
        self.assertEqual(r3.height, 3)
        self.assertEqual(r3.x, 4)
        self.assertEqual(r3.y, 5)
        r3.update(x=1, height=2, y=3, width=4)
        self.assertEqual(r3.width, 4)
        self.assertEqual(r3.height, 2)
        self.assertEqual(r3.x, 1)
        self.assertEqual(r3.y, 3)
