#!/usr/bin/python3
"""Unittest for max_integer([..])
"""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Test cases for max_integer function"""

    def test_regular_list(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_unordered_list(self):
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_max_at_beginning(self):
        """Max value is at the beginning of the list"""
        self.assertEqual(max_integer([9, 1, 2, 3]), 9)

    def test_negative_numbers(self):
        self.assertEqual(max_integer([-5, -2, -9]), -2)

    def test_single_element(self):
        self.assertEqual(max_integer([7]), 7)

    def test_empty_list(self):
        self.assertIsNone(max_integer([]))

    def test_none_argument(self):
        with self.assertRaises(TypeError):
            max_integer(None)

    def test_string_list(self):
        self.assertEqual(max_integer(["a", "z", "m"]), "z")

    def test_string(self):
        self.assertEqual(max_integer("Holberton"), "t")

    def test_mixed_types(self):
        with self.assertRaises(TypeError):
            max_integer([1, "2", 3])
