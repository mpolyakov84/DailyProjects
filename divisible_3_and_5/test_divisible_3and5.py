import unittest
from divisible_3and5 import divisible_3and5


class TestDivisible(unittest.TestCase):

    def test_divisible_3and5(self):
        expected_result = [15, 30, 45, 60, 75, 90]
        check = divisible_3and5(100)
        self.assertEqual(check, expected_result)
