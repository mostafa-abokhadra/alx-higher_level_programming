#!/usr/bin/python3
"""unit test for max integer module"""


import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """test class of the module"""

    def test_max(self):
        """testing nums 0, greater than zero and lesser"""
        self.assertAlmostEqual(max_integer([1, 2, 3, 4, 10]), 10)
        self.assertAlmostEqual(max_integer([-100, -200, -1]), -1)
        self.assertAlmostEqual(max_integer([-1, -2, -3, 0, -4]), 0)
        self.assertAlmostEqual(max_integer([845]), 845)

    def test_empty(self):
        """testing empty list"""
        self.assertAlmostEqual(max_integer([]), None)

    if __name__ == '__main__':
        unittest.main()
