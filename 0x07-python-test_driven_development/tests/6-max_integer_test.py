#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """testint class for max integer"""
    def test_max_integer(self):
        """max int test"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([1, 2, 5, 4]), 5)
        self.assertEqual(max_integer([1, 6, 3, 4]), 6)
        self.assertEqual(max_integer([7, 2, 3, 4]), 7)
        self.assertEqual(max_integer([1, -1, 3, 4]), 4)
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)
        self.assertEqual(max_integer([4]), 4)
        self.assertEqual(max_integer([]), None)
if __name__ == "__main__":
    unittest.main()
