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

if __name__ == "__main__":
    unittest.main()
