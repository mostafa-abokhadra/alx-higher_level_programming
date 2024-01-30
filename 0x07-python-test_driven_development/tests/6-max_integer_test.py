#!/usr/bin/python3
"""unit test for max integer module"""


import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """test class of the module"""

    def test_int(self):
        """testing nums 0, greater than zero and lesser"""
        self.assertAlmostEqual(max_integer([1, 2, 3, 4, 10]), 10)
        self.assertAlmostEqual(max_integer([-100, -200, -1]), -1)
        self.assertAlmostEqual(max_integer([-1, -2, -3, 0, -4]), 0)
        self.assertAlmostEqual(max_integer([845]), 845)

    def test_str(self):
        """testing strings"""
        self.assertAlmostEqual(max_integer(['a', 'b', 'c']), 'c')
        self.assertAlmostEqual(max_integer(["messi", "maradona", "ronaldinho"]), "ronaldinho")

    def test_float(self):
        """testing float"""
        self.assertAlmostEqual(max_integer([2.5, 66.7, 1.4]), 66.7)

    def test_lists(self):
        """testing lists"""
        self.assertAlmostEqual(max_integer([["messi"], ["messii"]]), ['messii'])
        self.assertAlmostEqual(max_integer([("messi", 10), ("messi", 19)]), ('messi', 19))



    def test_empty(self):
        """testing empty list"""
        self.assertAlmostEqual(max_integer([]), None)

    if __name__ == '__main__':
        unittest.main()
