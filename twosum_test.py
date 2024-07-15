import unittest

from twosum import two_sum


class TestStringMethods(unittest.TestCase):
    def test_example1(self):
        self.assertEqual(two_sum([2, 7, 11, 15], 9), [0, 1])

    def test_example2(self):
        self.assertEqual(two_sum([3, 2, 4], 6), [1, 2])

    def test_example3(self):
        self.assertEqual(two_sum([3, 3], 6), [0, 1])
