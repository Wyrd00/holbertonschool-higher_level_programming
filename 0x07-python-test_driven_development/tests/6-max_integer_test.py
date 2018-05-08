#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):

    def test_max(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([4, 4, 4, 4]), 4)
        self.assertEqual(max_integer([1]), 1)
        self.assertEqual(max_integer([1, 2, 2, 59, 1]), 59)

    def test_max_negative(self):
        self.assertEqual(max_integer([-5, 1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([-5, -5, -5]), -5)
        self.assertEqual(max_integer([-5, -4, -2, -4]), -2)

    def test_empty(self):
        self.assertIsNone(max_integer([]))

    def test_bool(self):
        self.assertEqual(max_integer([True, 42, False, 1, 2]), 42)

if __name__ == "__main__":
    unittest.main()
