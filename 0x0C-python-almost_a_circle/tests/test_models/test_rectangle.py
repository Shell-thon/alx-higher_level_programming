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
        """
        test 1
        """
        r0 = Rectangle(1, 2)
        self.assertEqual(r0.id, 1)

        r1 = Rectangle(10, 2)
        self.assertEqual(r1.id, 2)

        r2 = Rectangle(2, 10)
        self.assertEqual(r2.id, 3)

        r3 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r3.id, 12)

    def test_3(self):
        """
        test 3
        """
        r1 = Rectangle(3, 2)
        self.assertEqual(r1.area(), 6)

        r2 = Rectangle(2, 10)
        self.assertEqual(r2.area(), 20)

        r3 = Rectangle(8, 7, 0, 0, 12)
        self.assertEqual(r3.area(), 56)

if __name__ == '__main__':
    unittest.main()
