#!/usr/bin/python3
"""
test_square module
"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestRectangle(unittest.TestCase):
    """
    test class for Suqare class
    """
    def setUp(self):
        Base._Base__nb_objects = 0

    def test_1(self):
        """test 1"""
        s0 = Square(1)
        self.assertEqual(s0.id, 1)
        self.assertEqual(s0.width, 1)
        self.assertEqual(s0.height, 1)
        self.assertEqual(s0.x, 0)
        self.assertEqual(s0.y, 0)
        self.assertEqual(s0.__str__(), "[Square] (1) 0/0 - 1")
        self.assertEqual(s0.area(), 1)
        output = {'id': 1, 'x': 0, 'size': 1, 'y': 0}
        self.assertEqual(s0.to_dictionary(), output)


if __name__ == '__main__':
    unittest.main()
