from unittest import TestCase
from functions.gcd import gcd

class gcdFunctionTestCase(TestCase):
    def test_gcd1(self):
        self.assertEqual(5, gcd(10, 5))

    def test_gcd2(self):
        self.assertEqual(3, gcd(33, 27))

    def test_gcd3(self):
        self.assertEqual(9, gcd(99, 45))

    def test_gcd4(self):
        self.assertEqual(1, gcd(97, 23))

    def test_gcd5(self):
        self.assertEqual(10, gcd(10, 100))


