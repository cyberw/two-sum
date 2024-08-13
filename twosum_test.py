import unittest

from twosum import two_sum


class TestTwoSum(unittest.TestCase):
    def test_example1(self):
        self.assertEqual(two_sum([2, 7, 11, 15], 9), [0, 1])

    def test_example2(self):
        self.assertEqual(two_sum([3, 2, 4], 6), [1, 2])

    def test_example3(self):
        self.assertEqual(two_sum([3, 3], 6), [0, 1])

    def test_example4(self):
        self.assertEqual(two_sum([1, 4, 12, 5], 9), [1, 3])
if __name__ == "__main__":
    unittest.main()  # or you can run it using python -m unittest twosum_test.py
