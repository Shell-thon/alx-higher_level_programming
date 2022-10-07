#!/usr/bin/python3
"""
test_rectangle module
"""
import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """
    test class for Rectangle class
    """
    def setUp(self):
        Base._Base__nb_objects = 0

    def test_1(self):
        """test 1"""
        r0 = Rectangle(1, 2)
        self.assertEqual(r0.id, 1)
        self.assertEqual(r0.width, 1)
        self.assertEqual(r0.height, 2)
        self.assertEqual(r0.x, 0)
        self.assertEqual(r0.y, 0)
        self.assertEqual(r0.__str__(), "[Rectangle] (1) 0/0 - 1/2")

    def test_2(self):
        """test 2"""
        r0 = Rectangle(1, 2, 3)
        self.assertEqual(r0.id, 1)
        self.assertEqual(r0.width, 1)
        self.assertEqual(r0.height, 2)
        self.assertEqual(r0.x, 3)
        self.assertEqual(r0.y, 0)
        self.assertEqual(r0.__str__(), "[Rectangle] (1) 3/0 - 1/2")

if __name__ == '__main__':
    unittest.main()
