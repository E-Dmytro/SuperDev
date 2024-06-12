import unittest
# from parameterized import parameterized

from function_for_testing import divide

class Test1(unittest.TestCase):

    def test_possitive_devide(self):
        expected = 5
        actual = divide(10,2)
        self.assertEqual(actual, expected)

    def test_possitive_devide(self):
        expected = 0.5
        actual = divide(2, 4)
        self.assertEqual(actual, expected)

    def test_possitive_devide(self):
        expected = 0.333333
        actual = divide(1, 3)
        self.assertEqual(actual, expected,6
                         )

    def test_raises(self):
        self.assertRaises(Exception,divide,3,0)

    def other_function(self):
        self.assertTrue(False)
