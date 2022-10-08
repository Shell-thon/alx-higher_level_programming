#!/usr/bin/python3
"""
test_rectangle module
"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
from io import StringIO
import sys


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
        self.assertEqual(r0.area(), 2)
        capturedOutput = StringIO()
        sys.stdout = capturedOutput
        r0.display()
        sys.stdout = sys.__stdout__

        output = '#\n#\n'
        self.assertEqual(capturedOutput.getvalue(), output)
        output = {'x': 0, 'y': 0, 'id': 1, 'height': 2, 'width': 1}
        self.assertEqual(r0.to_dictionary(), output)
        r0.update()
        self.assertEqual(r0.__str__(), "[Rectangle] (1) 0/0 - 1/2")
        r0.update(89)
        self.assertEqual(r0.__str__(), "[Rectangle] (89) 0/0 - 1/2")
        r0.update(89, 1)
        self.assertEqual(r0.__str__(), "[Rectangle] (89) 0/0 - 1/2")
        r0.update(89, 1, 2)
        self.assertEqual(r0.__str__(), "[Rectangle] (89) 0/0 - 1/2")
        r0.update(89, 1, 2, 3)
        self.assertEqual(r0.__str__(), "[Rectangle] (89) 3/0 - 1/2")
        r0.update(89, 1, 2, 3, 4)
        self.assertEqual(r0.__str__(), "[Rectangle] (89) 3/4 - 1/2")
        r0.update(**{'id': 89})
        self.assertEqual(r0.__str__(), "[Rectangle] (89) 3/4 - 1/2")
        r0.update(**{'id': 89, 'width': 1})
        self.assertEqual(r0.__str__(), "[Rectangle] (89) 3/4 - 1/2")
        r0.update(**{'id': 89, 'width': 1, 'height': 2})
        self.assertEqual(r0.__str__(), "[Rectangle] (89) 3/4 - 1/2")
        r0.update(**{'id': 89, 'width': 1, 'height': 2, 'x': 3})
        self.assertEqual(r0.__str__(), "[Rectangle] (89) 3/4 - 1/2")
        r0.update(**{'id': 89, 'width': 1, 'height': 2, 'x': 3, 'y': 4})
        self.assertEqual(r0.__str__(), "[Rectangle] (89) 3/4 - 1/2")

    def test_2(self):
        """test 2"""
        r0 = Rectangle(1, 2, 3)
        self.assertEqual(r0.id, 1)
        self.assertEqual(r0.width, 1)
        self.assertEqual(r0.height, 2)
        self.assertEqual(r0.x, 3)
        self.assertEqual(r0.y, 0)
        self.assertEqual(r0.__str__(), "[Rectangle] (1) 3/0 - 1/2")
        self.assertEqual(r0.area(), 2)

    def test_3(self):
        """test 3"""
        r0 = Rectangle(1, 2, 3, 4)
        self.assertEqual(r0.id, 1)
        self.assertEqual(r0.width, 1)
        self.assertEqual(r0.height, 2)
        self.assertEqual(r0.x, 3)
        self.assertEqual(r0.y, 4)
        self.assertEqual(r0.__str__(), "[Rectangle] (1) 3/4 - 1/2")
        self.assertEqual(r0.area(), 2)

    def test_4(self):
        """test 4"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("1", 2)

    def test_5(self):
        """test 5"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, "2")

    def test_6(self):
        """test 6"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, "3")

    def test_7(self):
        """test 7"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 3, "4")

    def test_8(self):
        """test 8"""
        r0 = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(r0.id, 5)
        self.assertEqual(r0.width, 1)
        self.assertEqual(r0.height, 2)
        self.assertEqual(r0.x, 3)
        self.assertEqual(r0.y, 4)
        self.assertEqual(r0.__str__(), "[Rectangle] (5) 3/4 - 1/2")
        self.assertEqual(r0.area(), 2)

    def test_9(self):
        """test 9"""
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(-1, 2)

    def test_10(self):
        """test 10"""
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(1, -2)

    def test_11(self):
        """test 11"""
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(0, 2)

    def test_12(self):
        """test 12"""
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(1, 0)


if __name__ == '__main__':
    unittest.main()
