#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):

    def test_max(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_max_negative(self):
        self.assertEqual(max_integer([-5, 1, 2, 3, 4]), 4)

    def test_isdigit(self):
        self.assetFalse(max_integer([1, 'tehe', 3]).isdigit())

    def test_empty(self):
        self.assertIsNone(max_integer([]))

    def test_bool(self):
        self.assertEqual(max_integer([True, 42, False, 1, 2]), 42)

if __name__ == '__main__':
    unittest.main()
