#!/usr/bin/python3
""" """
import unittest
import pep8
from models.base import Base
from models.rectangle import Rectangle
class Testbase(unittest.TestCase):
    """ """
    def test_pep8_conformance(self):
        """Test that we conform to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/base.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_dictionary(self):
        re1 = Rectangle(10, 7, 2, 8, 70)
        dictionary = re1.to_dictionary()
        json_dictionary = Base.to_json_string([dictionary])
        self.assertEqual(type(json_dictionary), str)

    def test_dictionary_None(self):
        re1 = []
        dictionary = re1.to_dictionary()
        self.assertEqual(Base.to_json_dictionary([dictionary]), "[]")
