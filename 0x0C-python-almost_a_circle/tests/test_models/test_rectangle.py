#!/usr/bin/python3

import unittest

from models.rectangle import Rectangle
from models.base import Base
Rectangle = __import__('rectangle').Rectangle

class test_rectangle(unittest.TestCase):

    r1 = Rectangle(10, 2)
    r2 = Rectangle(2, 10)
    r3 = Rectangle(10, 2, 0, 0, 12)

    def check_width(self):
        self.assertEqual(r1.id, 1)
