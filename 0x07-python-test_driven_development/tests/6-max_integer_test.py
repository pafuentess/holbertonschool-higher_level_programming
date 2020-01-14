#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):

    def test_normal_list(self):
        lista = [1, 2, 3, 4]
        self.assertEqual(max_integer(lista), 4)

    def max_at_the_beginning(self):
        lista = [5, 4, 3, 2]
        self.assertEqual(max_integer(lista), 5)

    def list_of_one_element:
        lista = [5]
        self.assertEqual(max_integer(lista), 5)

    def test_with_string(self):
        with self.assertRaises(TypeError):
            lista = [1, "paula", 3, 4]
            max_integer(lista)

    def test_with_negative(self):
        lista = [1, 2, 3, -4]
        self.assertEqual(max_integer(lista), 3)

    def empty_list(self):
        lista = []
        self.assertIsNone(max_integer(lista))
